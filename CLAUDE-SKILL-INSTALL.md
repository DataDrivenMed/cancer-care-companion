# Install Cancer Care Companion as a Claude Skill

Cancer Care Companion can be installed as a true custom **Skill in Claude**, separate from the existing Claude Project option.

Claude custom Skills are uploaded as ZIP packages. Once enabled, Claude can use the Skill automatically when a request matches its purpose.

## Recommended: upload it as a custom Skill

### 1. Build the Claude Skill ZIP

From the repository root, run:

```bash
python3 scripts/package_claude_skill.py
```

This creates:

```text
dist/cancer-care-companion-claude-skill.zip
```

The ZIP is self-contained. It packages the core Skill instructions, quality checks, ClinicalTrials.gov helper, cancer-state schema, output templates, and disclaimer together.

### 2. Upload the Skill to Claude

In Claude:

1. Open **Customize**.
2. Open **Skills**.
3. Click the **+** button.
4. Choose **Create skill**.
5. Choose **Upload a skill**.
6. Upload `dist/cancer-care-companion-claude-skill.zip`.
7. Enable **Cancer Care Companion**.

If Claude asks you to enable **Code execution and file creation**, enable it in **Settings > Capabilities**. Organization-managed accounts may require an administrator to enable Skills.

Claude currently supports custom Skills on Free, Pro, Max, Team, and Enterprise plans, subject to organization settings where applicable.

Official Claude documentation: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## How to use it after installation

You do not need to paste the instructions into every chat. Ask naturally, for example:

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

Claude may also invoke the Skill automatically when a request clearly matches the Skill description.

## What is inside the uploaded Skill

The package script creates this structure:

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

The repository keeps the schema and templates in shared top-level folders, but the packaging script gathers them into the ZIP so the Claude Skill works as a self-contained package.

## Automatic packaging in GitHub Actions

The repository also includes:

```text
.github/workflows/package-claude-skill.yml
```

It builds the ZIP and uploads it as a GitHub Actions artifact whenever the packaged Skill components change on `main`. It can also be run manually with **workflow_dispatch**.

## Agent Skills CLI remains available

For Claude Code or other compatible agent environments that support the open Agent Skills CLI, you can still install directly from GitHub:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

This is a separate installation route from uploading a custom Skill ZIP into Claude chat.

## Keep the Claude Project option

The existing project-based setup remains in the repository:

```text
claude-instructions.md
```

Use the two modes differently:

| Mode | Best for |
| --- | --- |
| **Claude Skill** | Reusable Cancer Care Companion behavior available across Claude conversations |
| **Claude Project** | One patient's long-running workspace with reports, files, and persistent case context |

For an ongoing case, a strong pattern is to enable the **Cancer Care Companion Skill** and also keep that patient's documents in a dedicated Claude Project.

## Privacy

Follow the privacy and data-handling rules of the Claude account and organization being used. Do not place names, medical record numbers, dates of birth, exact addresses, insurance identifiers, or other direct patient identifiers into public web searches or clinical-trial search queries.
