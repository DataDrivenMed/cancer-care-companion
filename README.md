# Cancer Care Companion

> A longitudinal, evidence-grounded cancer navigation skill for patients and caregivers.

Cancer Care Companion builds on the concise patient-advocacy brief concept in [Peter Yang's `/fuck-cancer`](https://github.com/petergyang/fuck-cancer) and expands it into a modular cancer-navigation system.

The design goal is simple: **keep the patient-facing output short while making the intelligence behind it much deeper.**

## Start here

You do not need to understand the architecture before using Cancer Care Companion.

The basic workflow is:

1. **Install the skill or load the instructions into your AI workspace.**
2. **Start with whatever information you have.** A diagnosis, brain dump, pathology report, imaging report, molecular report, treatment summary, or existing cancer brief is enough.
3. **Ask Cancer Care Companion to build or update one living record.**
4. **Come back to the same record whenever something changes.** Upload the new report or describe the update and ask it to update the case.
5. **Generate the view you need right now.** Living Brief, Appointment Packet, Decision Map, Trial Shortlist, Biomarker Summary, Treatment Timeline, Second-Opinion Packet, or Caregiver Handoff.

See [`QUICKSTART.md`](./QUICKSTART.md) for a complete walkthrough.

## Installation

### Option 1: Agent Skills CLI

For tools that support the open Agent Skills format, install the skill from this repository:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

The `skills` CLI supports Git repositories and selecting a named skill with `--skill`. Global installation makes the skill available across projects for supported agents.

During development, before `comprehensive-v2` is merged into `main`, you can clone this branch and install it locally:

```bash
git clone -b comprehensive-v2 https://github.com/DataDrivenMed/cancer-care-companion.git
npx skills add ./cancer-care-companion --skill cancer-care-companion --global --yes
```

### Option 2: Claude Project

1. Create a Claude Project.
2. Open **Project Instructions**.
3. Copy the contents of [`claude-instructions.md`](./claude-instructions.md) into the project instructions.
4. Add the patient's de-identified reports or existing brief to the project when needed.
5. Start with a message such as:

```text
Build a Cancer Care Companion record from these reports and tell me the three things that matter most right now.
```

### Option 3: Any AI workspace that accepts persistent instructions

Use [`skills/cancer-care-companion/SKILL.md`](./skills/cancer-care-companion/SKILL.md) as the system/project instructions. Keep the same conversation, workspace, or designated source-of-truth file when updating a case so the longitudinal record remains coherent.

## Your first use

You can start with almost nothing.

### Start from a brain dump

```text
/cancer-care My mom was diagnosed with breast cancer last week. We know it is invasive ductal carcinoma. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us what matters next.
```

### Start from uploaded reports

Upload the reports, then type:

```text
/cancer-care Read these documents, reconcile the dates and findings, and create our living cancer record. Separate what is confirmed, pending, uncertain, and conflicting. Then give me the three most important next actions.
```

### Start from an existing `/fuck-cancer` brief

```text
/cancer-care Import this existing brief as the starting point. Preserve the concise patient-facing summary, but build the deeper longitudinal cancer state behind it.
```

## The most important rule: keep updating the same case

Cancer Care Companion is designed to be longitudinal. Do not start over every time a new result arrives.

When something changes, return to the same workspace or source of truth and say what changed.

### New pathology

```text
/cancer-care update Add this pathology report. Tell me exactly what changed from the previous understanding and whether it creates a new decision point.
```

### New imaging

```text
/cancer-care update Add this CT report. Compare it with the prior scan and update disease sites, response status, pending questions, and next actions.
```

### New molecular testing

```text
/cancer-care biomarkers Add this molecular report. Organize each finding by specimen, assay, date, result, and potential significance. Show what is actionable, what is uncertain, and what must be confirmed by the oncology team.
```

### Treatment change

```text
/cancer-care update The oncologist stopped regimen A and started regimen B today because of progression. Update the treatment timeline and explain what this changes in our living brief.
```

## What you can ask it to do

Subcommands are optional. Natural language works too.

| Command | Use it when you need | Example |
| --- | --- | --- |
| `/cancer-care` | General case navigation | `/cancer-care What are the three things we need to focus on now?` |
| `/cancer-care update` | Add a new report, visit, result, or treatment change | `/cancer-care update Add this PET report and update the case.` |
| `/cancer-care brief` | Short patient/caregiver summary | `/cancer-care brief Give me the current living brief.` |
| `/cancer-care appointment` | Prepare for a visit | `/cancer-care appointment Prepare us for Friday's oncology appointment.` |
| `/cancer-care decision` | Compare a real decision being discussed | `/cancer-care decision Map the two treatment options the oncologist discussed.` |
| `/cancer-care biomarkers` | Interpret and organize pathology/molecular findings | `/cancer-care biomarkers Explain this NGS report in the context of the case.` |
| `/cancer-care treatment` | Build or update treatment history | `/cancer-care treatment Create the treatment timeline with response and toxicity.` |
| `/cancer-care trials` | Screen for candidate clinical trials | `/cancer-care trials Find candidate trials within 150 miles for this treatment setting.` |
| `/cancer-care second-opinion` | Decide what type of outside review would help | `/cancer-care second-opinion What type of second opinion would be most useful now?` |
| `/cancer-care symptoms` | Organize a symptom and determine the safest escalation level | `/cancer-care symptoms She has new fever and chills after treatment. What should we do?` |
| `/cancer-care appeal` | Organize an insurance denial or appeal | `/cancer-care appeal Help us prepare an appeal for this denied scan.` |
| `/cancer-care caregiver` | Hand the case to another caregiver | `/cancer-care caregiver Create a handoff for my brother for the next seven days.` |
| `/cancer-care survivorship` | Transition into surveillance or long-term follow-up | `/cancer-care survivorship Build a surveillance and late-effects summary from this treatment history.` |

## Output modes

You do not need every output every time. Ask for the one that matches the immediate task.

### Living Brief

Use when you want the shortest useful summary.

It answers:

- What should we do next?
- What do we know?
- What is still uncertain?
- What should we ask next?

Example:

```text
/cancer-care brief Give me the one-page version I can take to appointments.
```

### Appointment Packet

Use before an oncology, surgery, radiation, genetics, pathology, or second-opinion visit.

It contains:

- what changed since the previous visit
- current treatment/status
- pending results
- the decision likely to be discussed
- up to five high-value questions
- reports or facts worth having available

Example:

```text
/cancer-care appointment We see the thoracic oncologist tomorrow. Build the appointment packet from the current record.
```

### Decision Map

Use when there is a real choice to discuss.

It separates:

- the decision being made
- realistic options
- why each might be considered
- evidence and major tradeoffs
- known patient-specific constraints
- unknowns that could change the choice
- what the care team needs to confirm

Example:

```text
/cancer-care decision The oncologist discussed surgery versus chemoradiation. Build a decision map without choosing for us.
```

### Biomarker Summary

Use for pathology, immunohistochemistry, molecular profiling, liquid biopsy, or germline testing.

Example:

```text
/cancer-care biomarkers Build a biomarker table from all reports. Keep older and newer results separate and flag contradictions.
```

### Treatment Timeline

Use to reconstruct therapy across months or years.

Example:

```text
/cancer-care treatment Build a chronological treatment timeline including intent, regimen, dates, response, toxicity, and reason for change when documented.
```

### Trial Shortlist

Use when clinical trials are relevant to the current disease and treatment setting.

Example:

```text
/cancer-care trials Find three to five candidate trials within 100 miles. Check the individual site's recruitment status and tell me what eligibility facts the trial team still needs to confirm.
```

Cancer Care Companion screens public trial information. It does not determine eligibility or select a treatment.

### Second-Opinion Packet

Use when you are considering outside review.

Example:

```text
/cancer-care second-opinion Build a concise packet for a molecular tumor board review and state the exact question we want them to answer.
```

### Caregiver Handoff

Use when another person needs to temporarily take over logistics.

Example:

```text
/cancer-care caregiver My sister is taking over for five days. Give her only the appointments, medications or treatment logistics already documented, pending items, contact tasks, and warning instructions she needs.
```

## A complete example

### Day 1: diagnosis

```text
/cancer-care My dad has newly diagnosed metastatic non-small-cell lung cancer. I uploaded the pathology and CT reports. Build the initial record and living brief.
```

Cancer Care Companion should establish what is confirmed, what is pending, the current disease picture, and the next three useful actions.

### Day 4: molecular report arrives

```text
/cancer-care biomarkers Add this NGS report to Dad's existing case. Tell me what changed and what questions it creates for the oncologist.
```

The new result is added without deleting the prior record.

### Day 6: oncology appointment

```text
/cancer-care appointment We meet the oncologist tomorrow. Prepare the appointment packet and five highest-value questions based on the entire case.
```

### Day 7: treatment options discussed

```text
/cancer-care decision The oncologist discussed these two approaches. Build a decision map using the information we already have and identify what still needs confirmation.
```

### Later: trial search

```text
/cancer-care trials Search for candidate trials within 150 miles that match the confirmed cancer type, biomarker, stage, and treatment setting. Do not claim eligibility.
```

This is the intended pattern: **one evolving case, many purpose-built views.**

## The two-layer model

### 1. Patient-facing layer

A short living brief that answers:

1. What should we do next?
2. What do we know?
3. What is still uncertain?
4. What should we ask at the next appointment?

### 2. Intelligence layer

A structured longitudinal record that tracks diagnosis, staging, pathology, biomarkers, treatment, response, symptoms, evidence, trials, practical barriers, documents, and unresolved decision points.

The brief is the front door. The structured cancer state is the engine behind it.

## Core capabilities

| Module | Purpose |
| --- | --- |
| Living Brief | Three immediate priorities, confirmed facts, terminology, compact care log |
| Cancer State | Longitudinal source of truth with current and historical disease facts |
| Diagnostic Navigator | Separates confirmed diagnosis, staging, pending workup, and meaningful gaps |
| Biomarker Intelligence | Organizes tumor, molecular, IHC, liquid-biopsy, and germline findings with provenance |
| Treatment Timeline | Tracks surgery, radiation, systemic therapy, cellular therapy, supportive care, response, and reasons for change |
| Decision Map | Shows the current decision node, realistic options to discuss, evidence, tradeoffs, and unknowns |
| Evidence Navigator | Grounds claims in official agencies, regulators, professional guidance, and primary literature |
| Trial Navigator | Finds candidate trials, checks site-level recruitment, and screens obvious eligibility mismatches without claiming eligibility |
| Second Opinions | Matches the clinical question to pathology, surgery, radiation, medical oncology, molecular tumor board, genetics, or trial review |
| Appointment Packet | Summarizes what changed, what is pending, and up to five high-value questions |
| Symptom Support | Organizes symptoms and uses care-team instructions plus context-aware escalation rather than universal hard-coded rules |
| Practical Navigation | Organizes insurance, travel, lodging, work, disability, financial support, rehabilitation, nutrition, fertility, and caregiver logistics |
| Survivorship | Transitions the same longitudinal record into surveillance and late-effect tracking when appropriate |
| Document Intelligence | Keeps extracted facts traceable to pathology, imaging, notes, molecular reports, labs, and other supplied records |

## Structured cancer state

The included JSON schema supports:

- cancer type and histology
- staging system, stage, and basis
- disease sites
- pathology
- biomarkers and molecular alterations
- germline results
- treatments and line/intent when documented
- response assessments
- symptoms and adverse effects
- pending studies
- decision points
- appointments
- clinical-trial candidates
- practical barriers
- source-document provenance
- contradictions and unresolved conflicts

A newer result never silently erases an older one. Conflicting records are surfaced for clarification.

## Evidence hierarchy

For current medical research, prefer:

1. national cancer agencies and official government sources
2. national regulators for approvals and labels
3. current official professional guidance when directly applicable
4. peer-reviewed primary evidence for unresolved or emerging questions
5. academic cancer-center pages for their own programs and trials
6. curated variant resources only as supplemental evidence

Do not present search snippets, SEO pages, social posts, or AI summaries as medical evidence.

## Symptom escalation

The companion does **not** use one universal oncology triage table for every patient. Escalation should consider:

- the oncology team's written instructions
- treatment type and timing
- immune suppression or other documented risk factors
- measured vital signs when available
- severity, duration, and progression
- inability to hydrate or take essential medication
- neurologic, respiratory, bleeding, or other emergency features

When the safest action is urgent evaluation, that action is placed first and research does not delay it.

## Privacy

Use the privacy rules of the environment in which the skill is running. Do not place names, medical record numbers, dates of birth, exact addresses, or other direct identifiers into public web searches or trial-search queries.

For consumer AI services, users should review the service's data controls and their organization's policies before entering protected or confidential health information. Do not make blanket claims that every AI service is or is not HIPAA compliant.

## Repository layout

```text
skills/cancer-care-companion/
  SKILL.md
  eval.md
  agents/openai.yaml
  scripts/search_trials.py
schemas/
  cancer-state.schema.json
templates/
  living-brief.md
  appointment-packet.md
  decision-map.md
tests/
  test_search_trials.py
QUICKSTART.md
claude-instructions.md
DISCLAIMER.md
LICENSE
```

## Status

`comprehensive-v2` is the expanded architecture. Initial implementation focuses on the longitudinal state model, safer symptom handling, patient/caregiver views, decision support, evidence provenance, trial screening, and reusable output templates.

## Attribution

This project is inspired by and builds on concepts from [`petergyang/fuck-cancer`](https://github.com/petergyang/fuck-cancer), Copyright (c) 2026 Peter Yang, licensed under the MIT License.

## License

MIT. See `LICENSE`.
