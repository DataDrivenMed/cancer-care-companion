import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "package_claude_skill.py"

spec = importlib.util.spec_from_file_location("package_claude_skill", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ClaudeSkillPackageTests(unittest.TestCase):
    def test_claude_description_within_limit(self):
        self.assertLessEqual(len(module.CLAUDE_DESCRIPTION), 200)

    def test_package_contains_required_files(self):
        original_dist = module.DIST
        original_zip_path = module.ZIP_PATH
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dist = Path(temp_dir)
                module.DIST = temp_dist
                module.ZIP_PATH = temp_dist / "cancer-care-companion-claude-skill.zip"
                zip_path = module.build()

                with zipfile.ZipFile(zip_path) as archive:
                    names = set(archive.namelist())

                required = {
                    "cancer-care-companion/SKILL.md",
                    "cancer-care-companion/eval.md",
                    "cancer-care-companion/scripts/search_trials.py",
                    "cancer-care-companion/schemas/cancer-state.schema.json",
                    "cancer-care-companion/templates/living-brief.md",
                    "cancer-care-companion/templates/appointment-packet.md",
                    "cancer-care-companion/templates/decision-map.md",
                    "cancer-care-companion/DISCLAIMER.md",
                }
                self.assertTrue(required.issubset(names), required - names)
        finally:
            module.DIST = original_dist
            module.ZIP_PATH = original_zip_path

    def test_packaged_skill_has_short_trigger_description(self):
        original_dist = module.DIST
        original_zip_path = module.ZIP_PATH
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dist = Path(temp_dir)
                module.DIST = temp_dist
                module.ZIP_PATH = temp_dist / "cancer-care-companion-claude-skill.zip"
                zip_path = module.build()

                with zipfile.ZipFile(zip_path) as archive:
                    text = archive.read("cancer-care-companion/SKILL.md").decode("utf-8")

                description_line = next(
                    line for line in text.splitlines() if line.startswith("description:")
                )
                description = description_line.split(":", 1)[1].strip()
                self.assertEqual(description, module.CLAUDE_DESCRIPTION)
                self.assertLessEqual(len(description), 200)
        finally:
            module.DIST = original_dist
            module.ZIP_PATH = original_zip_path


if __name__ == "__main__":
    unittest.main()
