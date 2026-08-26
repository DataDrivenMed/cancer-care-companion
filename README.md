# Cancer Care Companion

> A longitudinal, evidence-grounded cancer navigation system for patients and caregivers.

Cancer Care Companion builds on the concise patient-advocacy brief concept in [Peter Yang's `/fuck-cancer`](https://github.com/petergyang/fuck-cancer) and expands it into a modular cancer-navigation system.

The design goal is simple: **keep the patient-facing output short while making the intelligence behind it much deeper.**

## Start here

You do not need to understand the architecture before using Cancer Care Companion.

The basic workflow is:

1. **Choose how you want to use Cancer Care Companion.** Install it as a Claude Skill, put it in a Claude Project, configure it as a Custom GPT in ChatGPT, or use the dedicated ChatGPT Work instructions.
2. **Start with whatever information you have.** A diagnosis, brain dump, pathology report, imaging report, molecular report, treatment summary, or existing cancer brief is enough.
3. **Build one living cancer record.**
4. **Keep updating the same case whenever something changes.**
5. **Generate the view you need now.** Living Brief, Appointment Packet, Decision Map, Biomarker Summary, Treatment Timeline, Trial Shortlist, Second-Opinion Packet, Caregiver Handoff, or survivorship update.

For a nontechnical walkthrough, see [`QUICKSTART.md`](./QUICKSTART.md).

# Choose your setup

Cancer Care Companion can be used in four main ways.

| Setup | Best for | Instructions |
| --- | --- | --- |
| **Claude Skill** | Installing Cancer Care Companion as a reusable skill available across supported Claude workflows | [`CLAUDE-SKILL-INSTALL.md`](./CLAUDE-SKILL-INSTALL.md) |
| **Claude Project** | Keeping one patient's files, context, and instructions together inside a persistent Claude Project | [`claude-instructions.md`](./claude-instructions.md) |
| **ChatGPT Custom GPT** | Creating a dedicated Cancer Care Companion GPT with instructions, knowledge files, capabilities, and conversation starters | [`chatgpt-gpt-setup.md`](./chatgpt-gpt-setup.md) |
| **ChatGPT Work** | Creating and updating editable cancer-care artifacts from reports and existing case files | [`chatgpt-work-instructions.md`](./chatgpt-work-instructions.md) |

You can use more than one setup. For example, a caregiver might maintain the case in a persistent Claude Project while a clinical team uses the ChatGPT Work instructions to generate an appointment packet or structured decision artifact.

## Option 1: Install as a Claude Skill

Cancer Care Companion is packaged in the Agent Skills format under:

```text
skills/cancer-care-companion/
```

Install it from GitHub with:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

Then invoke it with natural language, for example:

```text
/cancer-care My mom was diagnosed with breast cancer last week. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us the three things that matter most now.
```

Full instructions: [`CLAUDE-SKILL-INSTALL.md`](./CLAUDE-SKILL-INSTALL.md)

## Option 2: Use a Claude Project

The original project-based setup remains available.

1. Create a Claude Project.
2. Open **Project Instructions**.
3. Copy [`claude-instructions.md`](./claude-instructions.md) into the project instructions.
4. Add de-identified case material when needed.
5. Keep returning to the same project as the case changes.

This setup is useful when one patient or family wants a persistent workspace containing the evolving case.

## Option 3: Configure a Custom GPT in ChatGPT

The repository includes a complete Custom GPT configuration with:

- GPT name
- description
- full Instructions text
- recommended Knowledge files
- recommended capabilities
- conversation starters
- a synthetic test case

Use:

[`chatgpt-gpt-setup.md`](./chatgpt-gpt-setup.md)

The GPT can then be used without requiring the user to remember command syntax. Example:

```text
I uploaded the pathology, CT report, and molecular testing. Build the longitudinal case and tell me what the next decision is.
```

**Availability note:** ChatGPT controls who can create new Custom GPTs based on workspace type and permissions. If your ChatGPT environment does not provide the GPT builder, use the ChatGPT Work setup below or a ChatGPT Project.

## Option 4: Use with ChatGPT Work

The repository includes a dedicated instruction set designed for ChatGPT Work:

[`chatgpt-work-instructions.md`](./chatgpt-work-instructions.md)

This setup focuses on creating and updating editable artifacts such as:

```text
<first-name>-living-brief.md
<first-name>-cancer-state.json
<first-name>-treatment-timeline.md
<first-name>-appointment-packet.md
<first-name>-decision-map.md
```

Typical Work request:

```text
Use the attached pathology, CT report, oncology note, and molecular report. Create a concise Living Brief, structured cancer-state file, and Treatment Timeline. Separate confirmed, pending, uncertain, conflicting, and historical information. Preserve source dates.
```

When a new result arrives:

```text
Update the attached Living Brief and cancer-state file using this new PET/CT report. Do not recreate them from scratch. Show exactly what changed and whether the new findings alter the current decision point.
```

# Your first use

You can start with almost nothing.

## Start from a brain dump

```text
/cancer-care My mom was diagnosed with breast cancer last week. We know it is invasive ductal carcinoma. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us what matters next.
```

## Start from uploaded reports

Upload the reports, then type:

```text
/cancer-care Read these documents, reconcile the dates and findings, and create our living cancer record. Separate what is confirmed, pending, uncertain, and conflicting. Then give me the three most important next actions.
```

## Start from an existing `/fuck-cancer` brief

```text
/cancer-care Import this existing brief as the starting point. Preserve the concise patient-facing summary, but build the deeper longitudinal cancer state behind it.
```

# The most important rule: keep updating the same case

Cancer Care Companion is designed to be longitudinal. Do not start over every time a new result arrives.

When something changes, return to the same case, workspace, source-of-truth document, or artifacts and update them.

## New pathology

```text
/cancer-care Update our case with this new pathology report. Tell me what changed, what is now confirmed, and whether any previous information conflicts with it.
```

## New scan

```text
/cancer-care Update the timeline and disease status with this CT report. Compare it with the previous scan and explain the meaningful change in plain English.
```

## New molecular or biomarker result

```text
/cancer-care biomarkers Add this NGS report to the case. Explain each clinically relevant finding, preserve the specimen and assay information, and tell me which current decisions it could affect.
```

## Treatment begins

```text
/cancer-care Add today's treatment plan to the Treatment Timeline. Keep treatment intent, drugs, schedule, monitoring, and expected decision points separate from anything that is still uncertain.
```

## After an oncology visit

```text
/cancer-care Update our record with these visit notes. Show what changed since the last version and update our three priorities.
```

# What can I ask it to do?

You do not need exact commands. Natural language is preferred. These labels are useful shortcuts.

| Request | What you get |
| --- | --- |
| `/cancer-care` | Build or update the longitudinal cancer record and Living Brief |
| `/cancer-care appointment` | Appointment Packet with changes, pending results, next decision, and questions |
| `/cancer-care decision` | Decision Map comparing realistic options and unresolved information |
| `/cancer-care biomarkers` | Structured explanation of pathology and molecular findings |
| `/cancer-care treatment` | Treatment Timeline with response, toxicity, and reasons for change |
| `/cancer-care trials` | Shortlist of plausible trial candidates with site-level status |
| `/cancer-care second-opinion` | Second-Opinion Packet focused on the question that needs another expert review |
| `/cancer-care symptoms` | Context-aware symptom organization and escalation support |
| `/cancer-care appeal` | Structured insurance-denial and appeal support |
| `/cancer-care caregiver` | Caregiver handoff with immediate logistics and watch items |
| `/cancer-care survivorship` | Transition the existing record into surveillance and survivorship tracking |

# Example workflow from diagnosis forward

A case might evolve like this.

### Day 1: diagnosis

```text
/cancer-care My dad has newly diagnosed lung adenocarcinoma. Here are the biopsy and CT reports. Build the case and tell us the three things that matter now.
```

Cancer Care Companion establishes the diagnosis, known disease extent, pending workup, immediate milestones, and a Living Brief.

### Day 5: molecular testing arrives

```text
/cancer-care biomarkers Add this NGS report. Update the case and tell me what this changes.
```

The new results are added without erasing the original pathology. Specimen, assay, date, alteration, and clinical context remain traceable.

### Day 7: oncology appointment

```text
/cancer-care appointment Prepare us for tomorrow. What changed, what is still unknown, what decision is likely coming, and what five questions should we ask?
```

### Day 8: two options are discussed

```text
/cancer-care decision The oncologist discussed these two treatment approaches. Build a Decision Map comparing them using the facts in our case and current evidence. Do not choose for us.
```

### Later: trial screening

```text
/cancer-care trials Find plausible trials within 150 miles that fit the diagnosis, stage, biomarker, and treatment setting we have documented. Tell me what the trial sites would still need to confirm.
```

### During treatment

```text
/cancer-care Update the Treatment Timeline with today's infusion and these laboratory results. Note the new symptoms and tell me whether anything warrants contacting the oncology team now.
```

The same case continues throughout the course of care.

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
| Symptom Support | Organizes symptoms and uses care-team instructions plus context-aware escalation rather than universal hard-coded rules |
| Practical Navigation | Organizes insurance, travel, lodging, work, disability, financial support, rehabilitation, nutrition, fertility, and caregiver logistics |
| Survivorship | Transitions the same longitudinal record into surveillance and late-effect tracking when appropriate |
| Document Intelligence | Keeps extracted facts traceable to pathology, imaging, notes, molecular reports, labs, and other supplied records |

# Output modes

The same underlying case can generate:

- **Living Brief**: shortest patient/caregiver summary
- **Appointment Packet**: visit preparation and questions
- **Decision Map**: options, evidence, tradeoffs, and unknowns
- **Trial Shortlist**: three to five candidate studies with site status
- **Second-Opinion Packet**: concise case summary plus exact review question
- **Treatment Timeline**: chronological therapy, response, and toxicity history
- **Biomarker Summary**: molecular findings with specimen, assay, date, and provenance
- **Caregiver Handoff**: immediate logistics and watch items
- **Survivorship Update**: surveillance and late-effect tracking

# Structured cancer state

The included JSON schema supports:

- cancer type and histology
- staging system, stage, and basis
- disease sites
- pathology
- biomarkers and molecular alterations
- germline results
- treatments and line or intent when documented
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

# Evidence hierarchy

For current medical research, prefer:

1. national cancer agencies and official government sources
2. national regulators for approvals and labels
3. current official professional guidance when directly applicable
4. peer-reviewed primary evidence for unresolved or emerging questions
5. academic cancer-center pages for their own programs and trials
6. curated variant resources only as supplemental evidence

Do not present search snippets, SEO pages, social posts, or AI summaries as medical evidence.

# Symptom escalation

Cancer Care Companion does not use one universal oncology triage table for every patient. Escalation should consider:

- the oncology team's written instructions
- treatment type and timing
- immune suppression or other documented risk factors
- measured vital signs when available
- severity, duration, and progression
- inability to hydrate or take essential medication
- neurologic, respiratory, bleeding, or other emergency features

When urgent evaluation is the safest action, that action comes first and research does not delay it.

# Privacy

Use the privacy rules of the environment in which Cancer Care Companion is running. Do not place names, medical record numbers, dates of birth, exact addresses, or other direct identifiers into public web searches or trial-search queries.

For consumer AI services, review the service's data controls and organizational policies before entering protected or confidential health information. Do not assume that all AI environments have the same privacy, retention, or compliance configuration.

# Repository layout

```text
skills/cancer-care-companion/
  SKILL.md
  eval.md
  agents/
    openai.yaml
  scripts/
    search_trials.py
schemas/
  cancer-state.schema.json
templates/
  living-brief.md
  appointment-packet.md
  decision-map.md
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
