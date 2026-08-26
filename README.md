# Cancer Care Companion

> A longitudinal, evidence-grounded cancer navigation system for patients and caregivers.

Cancer Care Companion builds on the concise patient-advocacy brief concept in [Peter Yang's `/fuck-cancer`](https://github.com/petergyang/fuck-cancer) and expands it into a modular cancer-navigation system.

The design goal is simple: **keep the patient-facing output short while making the intelligence behind it much deeper.**

## Download a Claude Skill ZIP

No Python, Git, terminal, or build step is required. Download one ZIP and upload it directly to Claude under **Customize → Skills → + → Create skill → Upload a skill**.

### [Download Cancer Care Companion Standard](https://github.com/DataDrivenMed/cancer-care-companion/releases/latest/download/cancer-care-companion-claude-skill.zip)

**Recommended for most users.** Full longitudinal cancer navigation with concise patient-facing outputs, appointments, decisions, biomarkers, trials, symptoms, practical support, and survivorship.

### [Download Cancer Care Companion Patient](https://github.com/DataDrivenMed/cancer-care-companion/releases/latest/download/cancer-care-companion-patient-claude-skill.zip)

**Simpler patient and caregiver edition.** Focuses on the three things that matter now, appointments, symptoms, treatment questions, second opinions, insurance, and practical support with less technical structure.

### [Download Cancer Care Companion Power User](https://github.com/DataDrivenMed/cancer-care-companion/releases/latest/download/cancer-care-companion-power-claude-skill.zip)

**Advanced edition.** Adds deeper longitudinal state management, source provenance, biomarker intelligence, treatment timelines, ClinicalTrials.gov screening, decision maps, evidence hierarchy, and advanced uncertainty handling.

[View all releases](https://github.com/DataDrivenMed/cancer-care-companion/releases)

## Start here

You can use Cancer Care Companion in four ways.

| Setup | Best for | Instructions |
| --- | --- | --- |
| **Claude Skill** | Installing Cancer Care Companion as a reusable custom Skill in Claude | [`CLAUDE-SKILL-INSTALL.md`](./CLAUDE-SKILL-INSTALL.md) |
| **Claude Project** | Keeping one patient's files, context, and instructions together in a persistent Claude Project | [`claude-instructions.md`](./claude-instructions.md) |
| **ChatGPT Custom GPT** | Creating a dedicated Cancer Care Companion GPT with Instructions, Knowledge, capabilities, and conversation starters | [`chatgpt-gpt-setup.md`](./chatgpt-gpt-setup.md) |
| **ChatGPT Work** | Creating and updating editable cancer-care artifacts from reports and case files | [`chatgpt-work-instructions.md`](./chatgpt-work-instructions.md) |

You can combine these. For example, enable the reusable **Claude Skill** and keep one patient's records inside a dedicated **Claude Project**.

For a nontechnical walkthrough, see [`QUICKSTART.md`](./QUICKSTART.md).

# Choose your setup

## Option 1: Install as a custom Claude Skill

This is the preferred route when you want Cancer Care Companion available as a reusable Skill inside Claude chat rather than only inside one Project.

For ordinary Claude users, use one of the direct release downloads above. You do not need to build anything yourself.

Then in Claude:

1. Open **Customize**.
2. Open **Skills**.
3. Click **+**.
4. Choose **Create skill**.
5. Choose **Upload a skill**.
6. Upload the ZIP you downloaded.
7. Enable the Skill.

Full web, iPhone/iPad, Android, Cowork, and developer instructions: [`CLAUDE-SKILL-INSTALL.md`](./CLAUDE-SKILL-INSTALL.md)

For maintainers or developers, the repository can rebuild all three uploadable ZIPs with:

```bash
python3 scripts/package_claude_skill.py
```

This creates:

```text
dist/cancer-care-companion-claude-skill.zip
dist/cancer-care-companion-patient-claude-skill.zip
dist/cancer-care-companion-power-claude-skill.zip
```

For Claude Code or other compatible developer environments, the Agent Skills CLI also remains available:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

## Option 2: Use a Claude Project

The project-based setup remains available and is useful for one long-running patient case.

1. Create a Claude Project.
2. Open **Project Instructions**.
3. Copy [`claude-instructions.md`](./claude-instructions.md) into the Project instructions.
4. Add case material according to the privacy rules of the account being used.
5. Keep returning to the same Project as the case changes.

A practical pattern is to use the global **Cancer Care Companion Skill** for behavior and a dedicated **Claude Project** for each persistent case.

## Option 3: Configure a Custom GPT in ChatGPT

The repository includes a complete ChatGPT Custom GPT setup:

[`chatgpt-gpt-setup.md`](./chatgpt-gpt-setup.md)

The GPT configuration is split into separate layers:

```text
chatgpt/
  INSTRUCTIONS.md
  KNOWLEDGE_MANIFEST.md
  actions/
    clinicaltrials-openapi.yaml
```

- `chatgpt/INSTRUCTIONS.md` defines how the GPT behaves.
- `chatgpt/KNOWLEDGE_MANIFEST.md` lists reusable reference files to upload as GPT Knowledge.
- `clinicaltrials-openapi.yaml` is an optional Action for the public ClinicalTrials.gov API v2.

The setup guide also includes the GPT name, description, conversation starters, recommended capabilities, testing scenarios, and privacy boundaries.

**Availability note:** ChatGPT controls who can create new Custom GPTs based on workspace type and permissions. If the GPT builder is unavailable, the same instructions can be used in a ChatGPT Project.

## Option 4: Use with ChatGPT Work

For artifact-oriented workflows, use:

[`chatgpt-work-instructions.md`](./chatgpt-work-instructions.md)

This is useful for creating and updating editable files such as:

```text
<first-name>-living-brief.md
<first-name>-cancer-state.json
<first-name>-treatment-timeline.md
<first-name>-appointment-packet.md
<first-name>-decision-map.md
```

# How Cancer Care Companion works

The basic workflow is:

1. **Start with whatever information you have.** A diagnosis, brain dump, pathology report, imaging report, molecular report, treatment summary, or existing cancer brief is enough.
2. **Build one longitudinal cancer record.**
3. **Keep updating the same case whenever something changes.**
4. **Preserve chronology and source provenance.**
5. **Generate the view needed for the current task.**

# Your first use

## Start from a brain dump

```text
My mom was diagnosed with breast cancer last week. We know it is invasive ductal carcinoma. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us what matters next.
```

## Start from uploaded reports

```text
Read these documents, reconcile the dates and findings, and create our longitudinal cancer record. Separate confirmed, reported, pending, uncertain, historical, and conflicting information. Then give me the three most important next actions.
```

## Start from an existing `/fuck-cancer` brief

```text
Import this existing brief as the starting point. Preserve the concise patient-facing summary, but build the deeper longitudinal cancer state behind it.
```

# The most important rule: keep updating the same case

Cancer Care Companion is designed to be longitudinal. Do not start over every time a new result arrives.

## New pathology

```text
Update the existing case with this new pathology report. Tell me what changed, what is now confirmed, and whether any earlier information conflicts with it.
```

## New imaging

```text
Add this CT report. Compare it with the prior scan and update disease sites, response status, pending questions, and next actions.
```

## New molecular testing

```text
Add this molecular report. Organize each finding by specimen, assay, date, result, and potential significance. Show what may be actionable, what is uncertain, and what the oncology team must still confirm.
```

## Treatment change

```text
The oncologist stopped regimen A and started regimen B today because of progression. Update the Treatment Timeline and explain what this changes in our Living Brief.
```

# What can I ask it to do?

You do not need exact commands. Natural language is preferred.

| Request | What you get |
| --- | --- |
| **Living Brief** | The shortest useful patient/caregiver summary |
| **Case Update** | Add a new report, result, visit, symptom, or treatment change |
| **Appointment Packet** | Changes, pending results, next decision, and up to five high-value questions |
| **Decision Map** | Comparison of realistic options and unresolved information |
| **Biomarker Summary** | Structured explanation of pathology and molecular findings |
| **Treatment Timeline** | Treatment, response, toxicity, and reasons for change |
| **Trial Shortlist** | Candidate trials with site-level status and eligibility uncertainties |
| **Second-Opinion Packet** | The exact question and records needed for outside review |
| **Symptom Support** | Context-aware symptom organization and escalation support |
| **Insurance Appeal** | Denial, evidence, deadline, and appeal organization |
| **Caregiver Handoff** | Immediate logistics and watch items for another caregiver |
| **Survivorship** | Surveillance and late-effect tracking in the same longitudinal record |

# Example workflow

### Diagnosis

```text
My dad has newly diagnosed lung adenocarcinoma. Here are the biopsy and CT reports. Build the case and tell us the three things that matter now.
```

### Molecular testing arrives

```text
Add this NGS report to Dad's existing case. Preserve the original pathology and tell me what this changes.
```

### Appointment preparation

```text
Prepare us for tomorrow's oncology appointment. What changed, what is still unknown, what decision is likely coming, and what five questions should we ask?
```

### Treatment decision

```text
The oncologist discussed these two treatment approaches. Build a Decision Map using the information already in the case and current evidence. Do not choose for us.
```

### Trial screening

```text
Find plausible trials within 150 miles that fit the documented diagnosis, stage, biomarker, and treatment setting. Tell me what the trial sites would still need to confirm.
```

This is the intended pattern: **one evolving case, many purpose-built views.**

# Two-layer model

## 1. Patient-facing layer

The Living Brief answers:

1. What should we do next?
2. What do we know?
3. What is still uncertain?
4. What decision is next?
5. What should we ask at the next appointment?

## 2. Intelligence layer

Behind the brief is a structured longitudinal record tracking diagnosis, staging, pathology, biomarkers, treatment, response, symptoms, evidence, trials, practical barriers, documents, and unresolved decision points.

The brief is the front door. The structured cancer state is the engine behind it.

# Core capabilities

| Module | Purpose |
| --- | --- |
| Living Brief | Three immediate priorities, confirmed facts, terminology, and compact care log |
| Cancer State | Longitudinal source of truth with current and historical disease facts |
| Diagnostic Navigator | Separates confirmed diagnosis, staging, pending workup, and meaningful gaps |
| Biomarker Intelligence | Organizes tumor, molecular, IHC, liquid-biopsy, and germline findings with provenance |
| Treatment Timeline | Tracks surgery, radiation, systemic therapy, cellular therapy, supportive care, response, and reasons for change |
| Decision Map | Shows the current decision node, realistic options to discuss, evidence, tradeoffs, and unknowns |
| Evidence Navigator | Grounds claims in official agencies, regulators, professional guidance, and primary literature |
| Trial Navigator | Finds candidate trials, checks site-level recruitment, and screens obvious mismatches without claiming eligibility |
| Second Opinions | Matches the clinical question to pathology, surgery, radiation, medical oncology, molecular tumor board, genetics, or trial review |
| Appointment Packet | Summarizes what changed, what is pending, and up to five high-value questions |
| Symptom Support | Uses care-team instructions plus context-aware escalation rather than universal hard-coded rules |
| Practical Navigation | Organizes insurance, travel, lodging, work, disability, support, rehabilitation, nutrition, fertility, and caregiver logistics |
| Survivorship | Transitions the same longitudinal record into surveillance and late-effect tracking |
| Document Intelligence | Keeps extracted facts traceable to pathology, imaging, notes, molecular reports, labs, and other supplied records |

# Structured cancer state

The JSON schema supports diagnosis, stage, disease sites, pathology, biomarkers, germline results, treatments, response, symptoms, pending studies, decision points, appointments, trial candidates, practical barriers, source provenance, and unresolved conflicts.

A newer result never silently erases an older one. Conflicting records are surfaced for clarification.

# Evidence hierarchy

For current medical research, prefer:

1. national cancer agencies and official government sources
2. national regulators for approvals and labels
3. current official professional guidance when directly applicable
4. peer-reviewed primary evidence for unresolved or emerging questions
5. academic cancer-center pages for their own programs and trials
6. curated molecular resources only as supplemental evidence

Do not present search snippets, SEO health pages, social posts, or AI summaries as medical evidence.

# Symptom escalation

Cancer Care Companion does not use one universal oncology triage table for every patient. Escalation should consider the oncology team's instructions, treatment type and timing, documented risk factors, measured vital signs when available, severity and progression, hydration, medication access, and neurologic, respiratory, bleeding, allergic, or other emergency features.

When urgent evaluation may be needed, the immediate action comes first and research does not delay it.

# Privacy

Use the privacy rules of the environment in which Cancer Care Companion is running.

Do not place names, medical record numbers, dates of birth, exact addresses, insurance identifiers, or other direct identifiers into public web searches or clinical-trial queries.

Do not put a real patient's private case record into reusable shared GPT Knowledge files or a shared Claude Skill package.

# Repository layout

```text
skills/
  cancer-care-companion/
    SKILL.md
    eval.md
    agents/openai.yaml
    scripts/search_trials.py
  cancer-care-companion-patient/
    SKILL.md
  cancer-care-companion-power/
    SKILL.md

schemas/
  cancer-state.schema.json

templates/
  living-brief.md
  appointment-packet.md
  decision-map.md

chatgpt/
  INSTRUCTIONS.md
  KNOWLEDGE_MANIFEST.md
  actions/clinicaltrials-openapi.yaml

scripts/
  package_claude_skill.py

.github/workflows/
  test.yml
  package-claude-skill.yml
  release-claude-skills.yml

CLAUDE-SKILL-INSTALL.md
claude-instructions.md
chatgpt-gpt-setup.md
chatgpt-work-instructions.md
QUICKSTART.md
DISCLAIMER.md
LICENSE
```

# Attribution

This project is inspired by and builds on concepts from [`petergyang/fuck-cancer`](https://github.com/petergyang/fuck-cancer), Copyright (c) 2026 Peter Yang, licensed under the MIT License.

# License

MIT. See [`LICENSE`](./LICENSE).
