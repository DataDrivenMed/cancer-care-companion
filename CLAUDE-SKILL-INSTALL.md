# Install Cancer Care Companion as a Claude Skill

Cancer Care Companion can be installed as a true custom **Skill in Claude**, separate from the existing Claude Project option.

Claude custom Skills are uploaded as ZIP packages. Once enabled, Claude can use the Skill automatically when a request matches its purpose.

## Easiest route for most people: Claude.ai

You do **not** need Claude Code, Git, Node, or a terminal to use Cancer Care Companion as a custom Skill in the Claude web app.

Anthropic currently supports Skills for Free, Pro, Max, Team, and Enterprise users. Skills require **Code execution and file creation** to be enabled. Team and Enterprise organizations may also require an administrator to enable Skills or user-created Skills.

### 1. Get the Cancer Care Companion Skill ZIP

The repository includes a packaging script:

```bash
python3 scripts/package_claude_skill.py
```

It creates:

```text
dist/cancer-care-companion-claude-skill.zip
```

The ZIP is self-contained. It packages the core Skill instructions, quality checks, ClinicalTrials.gov helper, cancer-state schema, output templates, and disclaimer together.

The repository also includes a GitHub Actions workflow that builds the same package as an artifact:

```text
.github/workflows/package-claude-skill.yml
```

If you are a nontechnical user, you only need the finished `cancer-care-companion-claude-skill.zip` file. You do not need to run the Python script yourself if someone has already built the ZIP for you.

### 2. Enable Skills on Claude.ai

For Free, Pro, and Max accounts:

1. Go to **claude.ai** and sign in.
2. Open **Settings**.
3. Select **Capabilities**.
4. Make sure **Code execution and file creation** is enabled.
5. Open **Customize → Skills**.

For Team and Enterprise accounts, an organization owner may need to enable both **Code execution and file creation** and **Skills** in the organization's Skills settings first.

### 3. Upload Cancer Care Companion

In Claude:

1. Open **Customize**.
2. Open **Skills**.
3. Click the **+** button.
4. Choose **Create skill**.
5. Choose **Upload a skill**.
6. Upload `cancer-care-companion-claude-skill.zip`.
7. Confirm that **Cancer Care Companion** appears in your Skills list.
8. Leave the Skill toggled **on**.

You install it once. You do not need to paste the full instructions into every chat.

Official Claude documentation: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## How to use it after installation

You do not need exact command syntax. Ask naturally, for example:

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

# Use Cancer Care Companion on iPhone, iPad, and Android

Cancer Care Companion is intended to be usable by ordinary Claude users, including people using Claude from a phone.

The easiest mobile workflow is to **install the Skill once on your Claude account through claude.ai**, then use the same account in the Claude mobile app.

## Recommended mobile setup

1. In a browser, open **claude.ai**.
2. Sign in with the same Claude account you use on your phone or tablet.
3. Follow the web instructions above to upload and enable Cancer Care Companion under **Customize → Skills**.
4. Install or update the official Claude app on your iPhone, iPad, or Android device.
5. Sign in with the same Claude account.
6. Start a conversation and explicitly ask Claude to use **Cancer Care Companion** the first time.

Example:

```text
Use Cancer Care Companion. I just received my dad's new PET/CT report. Compare it with the previous scan, update the case, and tell me what changed and what we should ask at Thursday's oncology appointment.
```

Attach the report from the phone when the Claude app's attachment control is available.

## Using it in Claude Cowork on mobile

Anthropic currently documents **Skills and plugins as supported in Claude Cowork on web and mobile**.

If your Claude mobile app shows **Cowork** in the composer:

1. Open the latest Claude app.
2. Select **Cowork** instead of ordinary Chat.
3. Attach the reports or case files you want Claude to work with.
4. Ask Claude to use **Cancer Care Companion**.

Example:

```text
Use Cancer Care Companion with these pathology and imaging reports. Update the longitudinal case, revise the Living Brief, and create an Appointment Packet for tomorrow.
```

Cowork can be especially useful when the task involves several reports or generated files.

Anthropic currently lists Cowork on web/mobile for Max, Team, and Enterprise plans, with Pro availability rolling out. If Cowork is not shown in the app, use Claude chat or claude.ai with the installed Skill.

Official Cowork web/mobile documentation: https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile

## If you cannot find Skills on your phone

The mobile app interface may not always expose every management control in the same place as claude.ai. You do not need to reinstall the Skill separately for every device.

Use this fallback:

1. Open **claude.ai** in Safari, Chrome, or another browser.
2. Sign in to the same account.
3. Open **Customize → Skills**.
4. Confirm **Cancer Care Companion** is present and enabled.
5. Return to the Claude mobile app and try again.
6. If necessary, update the mobile app to the latest version.

The key idea is: **install/manage the Skill at the account level, then use that same Claude account across supported web and mobile surfaces.**

# What is inside the uploaded Skill

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

# Automatic packaging in GitHub Actions

The repository includes:

```text
.github/workflows/package-claude-skill.yml
```

It builds the ZIP and uploads it as a GitHub Actions artifact whenever the packaged Skill components change on `main`. It can also be run manually with **workflow_dispatch**.

# Developer installation: Agent Skills CLI

For Claude Code or other compatible agent environments that support the open Agent Skills CLI, you can install directly from GitHub:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

Or from a local clone:

```bash
git clone https://github.com/DataDrivenMed/cancer-care-companion.git
cd cancer-care-companion
npx skills add . --skill cancer-care-companion --global --yes
```

This terminal-based route is **not required** for ordinary claude.ai, iOS, iPadOS, or Android users.

# Keep the Claude Project option

The existing project-based setup remains in the repository:

```text
claude-instructions.md
```

Use the two modes differently:

| Mode | Best for |
| --- | --- |
| **Claude Skill** | Reusable Cancer Care Companion behavior available across supported Claude conversations |
| **Claude Project** | One patient's long-running workspace with reports, files, and persistent case context |

For an ongoing case, a strong pattern is to enable the **Cancer Care Companion Skill** and also keep that patient's documents in a dedicated Claude Project.

# Verify the Skill

After installation, try:

```text
Use Cancer Care Companion. I have a newly diagnosed lung cancer case with a biopsy report, CT report, and molecular testing. Build the longitudinal record and tell me the current decision point.
```

Then test a second workflow:

```text
Use Cancer Care Companion to prepare an Appointment Packet from this case. Tell me what changed, what is pending, what decision is next, and the five questions most worth asking.
```

If Claude does not appear to use the Skill:

1. Open **Customize → Skills** on claude.ai.
2. Confirm Cancer Care Companion is toggled on.
3. Confirm **Code execution and file creation** is enabled.
4. Be explicit once: `Use the Cancer Care Companion skill for this request.`

# Privacy

Follow the privacy and data-handling rules of the Claude account and organization being used. Do not place names, medical record numbers, dates of birth, exact addresses, insurance identifiers, or other direct patient identifiers into public web searches or clinical-trial search queries.