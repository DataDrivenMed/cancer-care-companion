# Install Cancer Care Companion as a Claude Skill

Cancer Care Companion can be used as a true custom **Skill in Claude**, separate from the existing Claude Project option.

## Recommended: upload it as a custom Skill

Claude custom Skills are uploaded as ZIP packages. Once enabled, Claude can use the skill automatically when a request matches its purpose.

### 1. Build the Claude Skill ZIP

From the repository root, run:

```bash
python3 scripts/package_claude_skill.py
```

This creates:

```text
dist/cancer-care-companion-claude-skill.zip
```

The package contains the core `SKILL.md`, trial-search helper, evaluation rules, cancer-state schema, output templates, and disclaimer in one self-contained folder.

### 2. Upload it to Claude

In Claude:

1. Open **Customize**.
2. Open **Skills**.
3. Click the **+** button.
4. Choose **Create skill**.
5. Choose **Upload a skill**.
6. Upload `dist/cancer-care-companion-claude-skill.zip`.
7. Enable **Cancer Care Companion**.

If Claude asks you to enable **Code execution and file creation**, enable it in **Settings > Capabilities**. Organization-managed accounts may require an administrator to enable Skills.

## How to use it after installation

You do not need to paste the skill instructions into each chat. Ask naturally, for example:

```text
Use Cancer Care Companion to build a living cancer record from these reports and tell me the three things that matter most right now.
```

```text
Update our Cancer Care Companion record with this new pathology report. Show what changed, what is still pending, and what we should ask at Friday's appointment.
```

```text
Use Cancer Care Companion to prepare an appointment packet from this case.
```

```text
Use Cancer Care Companion to create a decision map comparing the options our oncologist discussed.
```

```text
Use Cancer Care Companion to screen ClinicalTrials.gov for candidate trials within 150 miles. Do not claim eligibility.
```

Claude may also invoke the Skill automatically when the request clearly matches its description.

## What the Claude Skill includes

The packaged Skill includes:

```text
cancer-care-companion/
  SKILL.md
  eval.md
  scripts/
    search_trials.py
  schemas/
    cancer-state.schema.json
  templates/
    living-brief.md
    appointment-packet.md
    decision-map.md
  DISCLAIMER.md
```

The package script intentionally gathers the repository-level schema and templates into the Skill ZIP so the uploaded Skill is self-contained.

## Keep the Claude Project option too

The existing `claude-instructions.md` remains available for people who prefer a long-running Claude Project with reports and case files kept together.

Use the two modes differently:

| Mode | Best for |
| --- | --- |
| **Claude Skill** | Reusable cancer-navigation behavior available across Claude conversations |
| **Claude Project** | One patient's long-running workspace with persistent case files and project instructions |

For a single ongoing cancer case, a useful pattern is to enable the **Cancer Care Companion Skill** and also keep that patient's documents inside a dedicated Claude Project.

## Privacy

Follow the privacy and data-handling rules of the Claude account and organization being used. Do not place direct patient identifiers into public web searches or trial-search queries.
