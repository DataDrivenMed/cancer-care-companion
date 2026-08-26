#!/usr/bin/env python3
"""Build a self-contained Claude custom Skill ZIP.

Run from the repository root:
    python3 scripts/package_claude_skill.py

Output:
    dist/cancer-care-companion-claude-skill.zip
"""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILL = ROOT / "skills" / "cancer-care-companion"
DIST = ROOT / "dist"
ZIP_PATH = DIST / "cancer-care-companion-claude-skill.zip"
PACKAGE_ROOT_NAME = "cancer-care-companion"

CLAUDE_DESCRIPTION = (
    "Maintain a longitudinal cancer record and create briefs, appointment prep, "
    "decision maps, trial shortlists, symptom guidance, and practical care navigation."
)

EXTRA_FILES = {
    ROOT / "schemas" / "cancer-state.schema.json": Path("schemas/cancer-state.schema.json"),
    ROOT / "templates" / "living-brief.md": Path("templates/living-brief.md"),
    ROOT / "templates" / "appointment-packet.md": Path("templates/appointment-packet.md"),
    ROOT / "templates" / "decision-map.md": Path("templates/decision-map.md"),
    ROOT / "DISCLAIMER.md": Path("DISCLAIMER.md"),
}


def claude_compatible_skill_text(text: str) -> str:
    """Keep the shared Skill source but shorten its Claude trigger description."""
    replacement = f"description: {CLAUDE_DESCRIPTION}"
    updated, count = re.subn(
        r"^description:.*$",
        replacement,
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise RuntimeError("SKILL.md does not contain a description frontmatter field")
    if len(CLAUDE_DESCRIPTION) > 200:
        raise RuntimeError("Claude Skill description exceeds 200 characters")
    return updated


def build() -> Path:
    DIST.mkdir(parents=True, exist_ok=True)

    if not SOURCE_SKILL.exists():
        raise FileNotFoundError(SOURCE_SKILL)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        package_root = temp / PACKAGE_ROOT_NAME
        shutil.copytree(SOURCE_SKILL, package_root)

        skill_path = package_root / "SKILL.md"
        skill_path.write_text(
            claude_compatible_skill_text(skill_path.read_text(encoding="utf-8")),
            encoding="utf-8",
        )

        for source, relative_destination in EXTRA_FILES.items():
            if not source.exists():
                raise FileNotFoundError(source)
            destination = package_root / relative_destination
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        if ZIP_PATH.exists():
            ZIP_PATH.unlink()

        with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package_root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(temp))

    print(f"Created {ZIP_PATH}")
    return ZIP_PATH


if __name__ == "__main__":
    build()
