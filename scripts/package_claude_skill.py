#!/usr/bin/env python3
"""Build upload-ready Claude custom Skill ZIPs.

Run from the repository root:
    python3 scripts/package_claude_skill.py

Outputs:
    dist/cancer-care-companion-claude-skill.zip
    dist/cancer-care-companion-patient-claude-skill.zip
    dist/cancer-care-companion-power-claude-skill.zip
"""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STANDARD_SOURCE = ROOT / "skills" / "cancer-care-companion"
PATIENT_SOURCE = ROOT / "skills" / "cancer-care-companion-patient"
POWER_SOURCE = ROOT / "skills" / "cancer-care-companion-power"


@dataclass(frozen=True)
class Variant:
    key: str
    source: Path
    package_root: str
    zip_name: str
    description: str
    extras: Dict[Path, Path]


COMMON_ADVANCED_EXTRAS = {
    ROOT / "schemas" / "cancer-state.schema.json": Path("schemas/cancer-state.schema.json"),
    ROOT / "templates" / "living-brief.md": Path("templates/living-brief.md"),
    ROOT / "templates" / "appointment-packet.md": Path("templates/appointment-packet.md"),
    ROOT / "templates" / "decision-map.md": Path("templates/decision-map.md"),
    ROOT / "DISCLAIMER.md": Path("DISCLAIMER.md"),
}

VARIANTS = (
    Variant(
        key="standard",
        source=STANDARD_SOURCE,
        package_root="cancer-care-companion",
        zip_name="cancer-care-companion-claude-skill.zip",
        description=(
            "Maintain a longitudinal cancer record and create briefs, appointment prep, "
            "decision maps, trial shortlists, symptom guidance, and practical care navigation."
        ),
        extras=COMMON_ADVANCED_EXTRAS,
    ),
    Variant(
        key="patient",
        source=PATIENT_SOURCE,
        package_root="cancer-care-companion-patient",
        zip_name="cancer-care-companion-patient-claude-skill.zip",
        description=(
            "A simpler cancer navigation companion for patients and caregivers focused on "
            "next steps, appointments, symptoms, treatment questions, and practical support."
        ),
        extras={
            ROOT / "templates" / "living-brief.md": Path("templates/living-brief.md"),
            ROOT / "templates" / "appointment-packet.md": Path("templates/appointment-packet.md"),
            ROOT / "DISCLAIMER.md": Path("DISCLAIMER.md"),
        },
    ),
    Variant(
        key="power",
        source=POWER_SOURCE,
        package_root="cancer-care-companion-power",
        zip_name="cancer-care-companion-power-claude-skill.zip",
        description=(
            "Advanced cancer navigation with longitudinal state, provenance, biomarker intelligence, "
            "treatment timelines, trial screening, decision maps, and evidence-grounded research."
        ),
        extras={
            **COMMON_ADVANCED_EXTRAS,
            ROOT / "skills" / "cancer-care-companion" / "eval.md": Path("eval.md"),
            ROOT / "skills" / "cancer-care-companion" / "scripts" / "search_trials.py": Path("scripts/search_trials.py"),
            ROOT / "QUICKSTART.md": Path("references/QUICKSTART.md"),
            ROOT / "CLAUDE-SKILL-INSTALL.md": Path("references/CLAUDE-SKILL-INSTALL.md"),
        },
    ),
)


def claude_compatible_skill_text(text: str, description: str) -> str:
    """Normalize the Claude trigger description and enforce Claude's concise metadata."""
    if len(description) > 200:
        raise RuntimeError("Claude Skill description exceeds 200 characters")
    updated, count = re.subn(
        r"^description:.*$",
        f"description: {description}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise RuntimeError("SKILL.md does not contain a description frontmatter field")
    return updated


def copy_extras(package_root: Path, extras: Dict[Path, Path]) -> None:
    for source, relative_destination in extras.items():
        if not source.exists():
            raise FileNotFoundError(source)
        destination = package_root / relative_destination
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def build_variant(variant: Variant) -> Path:
    if not variant.source.exists():
        raise FileNotFoundError(variant.source)

    DIST.mkdir(parents=True, exist_ok=True)
    zip_path = DIST / variant.zip_name

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        package_root = temp / variant.package_root
        shutil.copytree(variant.source, package_root)

        skill_path = package_root / "SKILL.md"
        skill_path.write_text(
            claude_compatible_skill_text(
                skill_path.read_text(encoding="utf-8"), variant.description
            ),
            encoding="utf-8",
        )

        copy_extras(package_root, variant.extras)

        if zip_path.exists():
            zip_path.unlink()

        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package_root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(temp))

    print(f"Created {zip_path}")
    return zip_path


def build_all() -> list[Path]:
    return [build_variant(variant) for variant in VARIANTS]


if __name__ == "__main__":
    build_all()
