import argparse
import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).parents[1] / "skills" / "cancer-care-companion" / "scripts" / "search_trials.py"
spec = importlib.util.spec_from_file_location("search_trials", MODULE_PATH)
search_trials = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(search_trials)


class TrialSearchTests(unittest.TestCase):
    def test_country_alias(self):
        self.assertEqual(search_trials.normalize_country("USA"), "United States")

    def test_state_alias(self):
        self.assertEqual(search_trials.normalize_state("LA"), "Louisiana")

    def test_parse_near(self):
        self.assertEqual(search_trials.parse_near("29.95,-90.07"), (29.95, -90.07))

    def test_distance(self):
        distance = search_trials.haversine_miles((29.9511, -90.0715), 30.4515, -91.1871)
        self.assertGreater(distance, 60)
        self.assertLess(distance, 90)

    def test_closed_site_is_excluded(self):
        args = argparse.Namespace(
            country="United States",
            state="Louisiana",
            city="",
            near=None,
            radius_miles=100.0,
        )
        location = {
            "status": "ACTIVE_NOT_RECRUITING",
            "country": "United States",
            "state": "Louisiana",
            "city": "New Orleans",
        }
        self.assertFalse(search_trials.location_matches(location, args, "RECRUITING"))

    def test_open_site_is_included(self):
        args = argparse.Namespace(
            country="United States",
            state="Louisiana",
            city="",
            near=None,
            radius_miles=100.0,
        )
        location = {
            "status": "RECRUITING",
            "country": "United States",
            "state": "Louisiana",
            "city": "New Orleans",
        }
        self.assertTrue(search_trials.location_matches(location, args, "RECRUITING"))

    def test_relevance_prefers_matching_biomarker(self):
        args = argparse.Namespace(condition="lung adenocarcinoma", terms="EGFR")
        matching = {
            "title": "EGFR targeted study in lung adenocarcinoma",
            "interventions": ["osimertinib"],
            "eligibility_criteria": "EGFR mutation required",
            "overall_status": "RECRUITING",
            "phases": ["PHASE2"],
            "nct_id": "NCT1",
        }
        generic = {
            "title": "Supportive study in lung cancer",
            "interventions": ["survey"],
            "eligibility_criteria": "lung cancer",
            "overall_status": "RECRUITING",
            "phases": [],
            "nct_id": "NCT2",
        }
        ranked = search_trials.rank_trials([generic, matching], args)
        self.assertEqual(ranked[0]["nct_id"], "NCT1")


if __name__ == "__main__":
    unittest.main()
