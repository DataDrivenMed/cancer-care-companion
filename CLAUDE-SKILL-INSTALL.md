# Install Cancer Care Companion as a Claude Skill

Cancer Care Companion is packaged in the Agent Skills format under:

```text
skills/cancer-care-companion/
```

This is the preferred setup when you want the capability installed as a reusable **skill** rather than copied into a single Claude Project.

## Option 1: Install from GitHub

For Claude environments that support Agent Skills through the `skills` CLI:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

Global installation makes the skill available across supported projects and workspaces on that machine.

## Option 2: Install from a local clone

```bash
git clone https://github.com/DataDrivenMed/cancer-care-companion.git
cd cancer-care-companion
npx skills add . --skill cancer-care-companion --global --yes
```

## Verify the skill

After installation, start a new Claude session in an environment that supports installed skills and invoke it with natural language, for example:

```text
/cancer-care My mom was diagnosed with breast cancer last week. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us the three things that matter most now.
```

Or upload reports and say:

```text
/cancer-care Read these reports, reconcile the chronology, and update our longitudinal cancer record. Separate confirmed, pending, uncertain, and conflicting information.
```

## What the skill contains

The installed skill uses:

- `skills/cancer-care-companion/SKILL.md` for the operating workflow
- `skills/cancer-care-companion/eval.md` for quality checks
- `skills/cancer-care-companion/scripts/search_trials.py` for ClinicalTrials.gov searches
- `schemas/cancer-state.schema.json` for longitudinal case structure
- `templates/` for reusable output formats

## Keep the Claude Project option too

If you prefer a single persistent Claude Project instead of installing a reusable skill, the repository still includes:

```text
claude-instructions.md
```

Paste that file into Claude Project Instructions and keep the patient's case material in the same project.

## Recommended workflow

1. Install the skill once.
2. Start one case with whatever information is available.
3. Keep updating the same case when new pathology, imaging, biomarkers, treatments, or appointments occur.
4. Ask for the output you need: Living Brief, Appointment Packet, Decision Map, Biomarker Summary, Trial Shortlist, Second-Opinion Packet, Treatment Timeline, or Caregiver Handoff.

## Privacy

Do not place direct patient identifiers into public web searches or clinical-trial search queries. Follow the privacy and data-handling rules of the Claude environment and organization in which the skill is being used.
