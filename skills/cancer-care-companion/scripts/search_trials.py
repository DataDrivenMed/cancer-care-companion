#!/usr/bin/env python3
"""Search ClinicalTrials.gov API v2 for potentially relevant cancer trials.

This is a screening utility. It does not determine eligibility, recommend
therapy, or replace confirmation by the trial site and treating oncology team.
Do not place patient identifiers in query arguments.

Conceptually derived from the trial-search workflow in petergyang/fuck-cancer
(MIT License, Copyright 2026 Peter Yang), with expanded structured output.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

API_ROOT = "https://clinicaltrials.gov/api/v2/studies"
OPEN_STATUSES = {"RECRUITING", "NOT_YET_RECRUITING", "ENROLLING_BY_INVITATION"}
EARTH_RADIUS_MILES = 3958.8

COUNTRY_ALIASES = {
    "us": "United States",
    "usa": "United States",
    "u.s.": "United States",
    "uk": "United Kingdom",
    "u.k.": "United Kingdom",
}

STATE_ALIASES = {
    "al": "Alabama", "ak": "Alaska", "az": "Arizona", "ar": "Arkansas",
    "ca": "California", "co": "Colorado", "ct": "Connecticut", "de": "Delaware",
    "fl": "Florida", "ga": "Georgia", "hi": "Hawaii", "id": "Idaho",
    "il": "Illinois", "in": "Indiana", "ia": "Iowa", "ks": "Kansas",
    "ky": "Kentucky", "la": "Louisiana", "me": "Maine", "md": "Maryland",
    "ma": "Massachusetts", "mi": "Michigan", "mn": "Minnesota", "ms": "Mississippi",
    "mo": "Missouri", "mt": "Montana", "ne": "Nebraska", "nv": "Nevada",
    "nh": "New Hampshire", "nj": "New Jersey", "nm": "New Mexico", "ny": "New York",
    "nc": "North Carolina", "nd": "North Dakota", "oh": "Ohio", "ok": "Oklahoma",
    "or": "Oregon", "pa": "Pennsylvania", "ri": "Rhode Island", "sc": "South Carolina",
    "sd": "South Dakota", "tn": "Tennessee", "tx": "Texas", "ut": "Utah",
    "vt": "Vermont", "va": "Virginia", "wa": "Washington", "wv": "West Virginia",
    "wi": "Wisconsin", "wy": "Wyoming", "dc": "District of Columbia", "pr": "Puerto Rico",
}

STOPWORDS = {
    "a", "an", "and", "cancer", "carcinoma", "for", "in", "of", "or",
    "study", "the", "trial", "tumor", "tumour", "with",
}


def clean(value: Any) -> str:
    return " ".join(str(value or "").split())


def normalize_country(value: str) -> str:
    value = clean(value)
    return COUNTRY_ALIASES.get(value.casefold(), value)


def normalize_state(value: str) -> str:
    value = clean(value)
    return STATE_ALIASES.get(value.casefold(), value)


def parse_near(value: Optional[str]) -> Optional[Tuple[float, float]]:
    if not value:
        return None
    parts = [part.strip() for part in value.split(",")]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("--near must be LAT,LON")
    try:
        lat, lon = float(parts[0]), float(parts[1])
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--near must contain numeric coordinates") from exc
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise argparse.ArgumentTypeError("--near coordinates are out of range")
    return lat, lon


def haversine_miles(origin: Tuple[float, float], lat: float, lon: float) -> float:
    lat1, lon1 = map(math.radians, origin)
    lat2, lon2 = math.radians(lat), math.radians(lon)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * EARTH_RADIUS_MILES * math.asin(math.sqrt(a))


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", clean(text).casefold())
        if len(token) > 1 and token not in STOPWORDS
    }


def request_json(url: str) -> Dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "cancer-care-companion/2.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def build_query(args: argparse.Namespace, page_token: Optional[str] = None) -> str:
    location = ", ".join(part for part in [args.city, args.state, args.country] if part)
    params = {
        "query.cond": args.condition,
        "filter.overallStatus": "|".join(sorted(OPEN_STATUSES)),
        "format": "json",
        "pageSize": str(args.page_size),
    }
    if args.terms:
        params["query.term"] = args.terms
    if location:
        params["query.locn"] = location
    if args.near:
        lat, lon = args.near
        params["filter.geo"] = f"distance({lat},{lon},{args.radius_miles}mi)"
    if page_token:
        params["pageToken"] = page_token
    return API_ROOT + "?" + urllib.parse.urlencode(params)


def fetch_studies(args: argparse.Namespace) -> List[Dict[str, Any]]:
    studies: List[Dict[str, Any]] = []
    token: Optional[str] = None
    for _ in range(args.max_pages):
        payload = request_json(build_query(args, token))
        studies.extend(payload.get("studies", []))
        token = payload.get("nextPageToken")
        if not token:
            break
    return studies


def location_matches(location: Dict[str, Any], args: argparse.Namespace, overall_status: str) -> bool:
    status = clean(location.get("status")).upper()
    if status and status not in OPEN_STATUSES:
        return False
    if not status and overall_status.upper() not in OPEN_STATUSES:
        return False

    for field in ("country", "state", "city"):
        wanted = clean(getattr(args, field, ""))
        actual = clean(location.get(field))
        if wanted and actual.casefold() != wanted.casefold():
            return False

    if args.near:
        point = location.get("geoPoint") or {}
        try:
            distance = haversine_miles(args.near, float(point["lat"]), float(point["lon"]))
        except (KeyError, TypeError, ValueError):
            return False
        if distance > args.radius_miles:
            return False
    return True


def extract_trial(study: Dict[str, Any], args: argparse.Namespace) -> Optional[Dict[str, Any]]:
    protocol = study.get("protocolSection", {})
    ident = protocol.get("identificationModule", {})
    status_mod = protocol.get("statusModule", {})
    design = protocol.get("designModule", {})
    arms = protocol.get("armsInterventionsModule", {})
    elig = protocol.get("eligibilityModule", {})
    contacts = protocol.get("contactsLocationsModule", {})

    overall_status = clean(status_mod.get("overallStatus"))
    matching_locations = [
        loc for loc in contacts.get("locations", [])
        if location_matches(loc, args, overall_status)
    ]
    if not matching_locations:
        return None

    sites = []
    for loc in matching_locations:
        site = {
            "facility": clean(loc.get("facility")),
            "status": clean(loc.get("status")) or f"not listed; study {overall_status}",
            "city": clean(loc.get("city")),
            "state": clean(loc.get("state")),
            "country": clean(loc.get("country")),
        }
        if args.near:
            point = loc.get("geoPoint") or {}
            try:
                site["distance_miles"] = round(
                    haversine_miles(args.near, float(point["lat"]), float(point["lon"])), 1
                )
            except (KeyError, TypeError, ValueError):
                site["distance_miles"] = None
        sites.append(site)

    if args.near:
        sites.sort(key=lambda item: item.get("distance_miles") if item.get("distance_miles") is not None else 10**9)

    nct_id = clean(ident.get("nctId"))
    interventions = arms.get("interventions", [])
    criteria = clean(elig.get("eligibilityCriteria"))
    if not args.full_criteria and len(criteria) > args.criteria_chars:
        criteria = criteria[: args.criteria_chars].rstrip() + " [truncated]"

    return {
        "nct_id": nct_id,
        "url": f"https://clinicaltrials.gov/study/{nct_id}",
        "title": clean(ident.get("briefTitle")),
        "overall_status": overall_status,
        "phases": design.get("phases", []),
        "study_type": clean(design.get("studyType")),
        "interventions": [clean(i.get("name")) for i in interventions if clean(i.get("name"))],
        "intervention_types": sorted({clean(i.get("type")) for i in interventions if clean(i.get("type"))}),
        "minimum_age": clean(elig.get("minimumAge")),
        "maximum_age": clean(elig.get("maximumAge")),
        "sex": clean(elig.get("sex")),
        "eligibility_criteria": criteria,
        "open_sites": sites,
    }


def relevance_score(trial: Dict[str, Any], args: argparse.Namespace) -> int:
    cond = tokens(args.condition)
    terms = tokens(args.terms)
    title = tokens(trial.get("title", ""))
    interventions = tokens(" ".join(trial.get("interventions", [])))
    criteria = tokens(trial.get("eligibility_criteria", ""))

    score = 3 * len(cond & title) + 2 * len(cond & interventions) + len(cond & criteria)
    score += 5 * len(terms & title) + 3 * len(terms & interventions) + 2 * len(terms & criteria)
    if trial.get("overall_status") == "RECRUITING":
        score += 3
    phases = {clean(x).upper() for x in trial.get("phases", [])}
    if "PHASE3" in phases:
        score += 3
    elif "PHASE2" in phases:
        score += 2
    return score


def rank_trials(trials: Iterable[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    return sorted(trials, key=lambda trial: (-relevance_score(trial, args), trial.get("nct_id", "")))


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--condition", required=True, help="Cancer type or condition")
    parser.add_argument("--terms", default="", help="Stage, biomarker, treatment setting, or prior therapy")
    parser.add_argument("--country", required=True)
    parser.add_argument("--state", default="")
    parser.add_argument("--city", default="")
    parser.add_argument("--near", type=parse_near, default=None, help="LAT,LON")
    parser.add_argument("--radius-miles", type=float, default=100.0)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=5)
    parser.add_argument("--criteria-chars", type=int, default=2500)
    parser.add_argument("--full-criteria", action="store_true")
    args = parser.parse_args(argv)
    args.country = normalize_country(args.country)
    args.state = normalize_state(args.state)
    return args


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    try:
        studies = fetch_studies(args)
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 1

    extracted = []
    for study in studies:
        trial = extract_trial(study, args)
        if trial:
            extracted.append(trial)

    ranked = rank_trials(extracted, args)[: max(args.limit, 0)]
    output = {
        "screening_only": True,
        "eligibility_not_determined": True,
        "query": {
            "condition": args.condition,
            "terms": args.terms,
            "country": args.country,
            "state": args.state,
            "city": args.city,
            "near": args.near,
            "radius_miles": args.radius_miles if args.near else None,
        },
        "result_count": len(ranked),
        "results": ranked,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
