# Cancer Care Companion

> A longitudinal, evidence-grounded cancer navigation system for patients and caregivers.

Cancer Care Companion builds on the concise patient-advocacy brief concept in [Peter Yang's `/fuck-cancer`](https://github.com/petergyang/fuck-cancer) and expands it into a modular cancer-navigation system.

The design goal is simple: **keep the patient-facing output short while making the intelligence behind it much deeper.**

## Start here

You can use Cancer Care Companion in three primary ways:

| Platform | Installation | Best use |
| --- | --- | --- |
| **Claude Skill** | Upload the packaged custom Skill ZIP in Claude | Reusable Cancer Care Companion capability across Claude conversations |
| **ChatGPT Custom GPT** | Configure a dedicated GPT with the supplied Instructions, Knowledge files, and capabilities | Product-style Cancer Care Companion experience in ChatGPT |
| **Claude Project** | Paste the existing project instructions into a dedicated Claude Project | One long-running patient case with documents kept together |

The underlying cancer-navigation logic is shared. The installation method changes how the user accesses it.

### Claude Skill

Use this if you want Cancer Care Companion installed as a true custom **Skill in Claude**.

Full instructions: [`CLAUDE_SKILL_INSTALL.md`](./CLAUDE_SKILL_INSTALL.md)

Build the uploadable Skill ZIP with:

```bash
python3 scripts/package_claude_skill.py
```

This creates:

```text
dist/cancer-care-companion-claude-skill.zip
```

Then upload the ZIP in Claude through **Customize > Skills > + > Create skill > Upload a skill** and enable it.

Once installed, ask naturally:

```text
Use Cancer Care Companion to build a living cancer record from these reports and tell me the three things that matter most right now.
```

### ChatGPT Custom GPT

Use this if you want Cancer Care Companion configured as a dedicated **GPT in ChatGPT**.

Full instructions: [`CHATGPT_GPT_SETUP.md`](./CHATGPT_GPT_SETUP.md)

The repository includes:

```text
chatgpt/
  INSTRUCTIONS.md
  KNOWLEDGE_MANIFEST.md
  actions/
    clinicaltrials-openapi.yaml
```

The setup guide provides the GPT name, description, conversation starters, recommended capabilities, Knowledge files, testing scenarios, and an optional ClinicalTrials.gov Action.

> OpenAI currently limits creation of new Custom GPTs to eligible Business, Enterprise, and Edu workspaces, subject to workspace permissions. If **Create** is not available in the GPTs area, the same instructions can be used in a ChatGPT Project instead.

### Claude Project

Keep using the existing Claude Project route when you want one dedicated workspace for a patient's evolving case.

1. Create a Claude Project.
2. Open **Project Instructions**.
3. Copy [`claude-instructions.md`](./claude-instructions.md) into the Project instructions.
4. Add the patient's reports or existing brief as appropriate for the account and privacy requirements.
5. Continue using the same Project as new information arrives.

A strong Claude workflow is to **enable the Cancer Care Companion Skill globally and also use a dedicated Project for each long-running case**.

### Agent Skills CLI

For compatible agents and developer tools that support the open Agent Skills format:

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

## How Cancer Care Companion works

The basic workflow is:

1. **Start with whatever information you have.** A diagnosis, brain dump, pathology report, imaging report, molecular report, treatment summary, or existing cancer brief is enough.
2. **Build one longitudinal cancer record.**
3. **Update the same case whenever something changes.**
4. **Preserve old and new findings rather than silently overwriting history.**
5. **Generate the view needed for the current task.**

See [`QUICKSTART.md`](./QUICKSTART.md) for a complete walkthrough.

## Your first use

### Start from a brain dump

```text
My mom was diagnosed with breast cancer last week. We know it is invasive ductal carcinoma. We are waiting for HER2 testing and meet the oncologist Friday. Build our living brief and tell us what matters next.
```

### Start from uploaded reports

```text
Read these documents, reconcile the dates and findings, and create our longitudinal cancer record. Separate what is confirmed, reported, pending, uncertain, historical, and conflicting. Then give me the three most important next actions.
```

### Start from an existing `/fuck-cancer` brief

```text
Import this existing brief as the starting point. Preserve the concise patient-facing summary, but build the deeper longitudinal cancer state behind it.
```

## The most important rule: keep updating the same case

Cancer Care Companion is designed to be longitudinal. Do not start over every time a new result arrives.

### New pathology

```text
Update the existing case with this pathology report. Tell me exactly what changed from the previous understanding and whether it creates a new decision point.
```

### New imaging

```text
Add this CT report. Compare it with the prior scan and update disease sites, response status, pending questions, and next actions.
```

### New molecular testing

```text
Add this molecular report. Organize each finding by specimen, assay, date, result, and potential significance. Show what may be actionable, what is uncertain, and what the oncology team must still confirm.
```

### Treatment change

```text
The oncologist stopped regimen A and started regimen B today because of progression. Update the treatment timeline and explain what this changes in the living brief.
```

## What you can ask it to do

Natural language is preferred. `/cancer-care` style prompts are optional convenience shorthand.

| Request | Use it when you need |
| --- | --- |
| **Living Brief** | The shortest useful patient/caregiver summary |
| **Case Update** | Add a new report, result, visit, symptom, or treatment change |
| **Appointment Packet** | Prepare for oncology, surgery, radiation, genetics, pathology, or second-opinion visits |
| **Decision Map** | Compare realistic options currently being discussed |
| **Biomarker Summary** | Organize pathology, IHC, molecular, liquid-biopsy, or germline findings |
| **Treatment Timeline** | Reconstruct treatment, response, toxicity, and reasons for change |
| **Trial Shortlist** | Screen candidate clinical trials without claiming eligibility |
| **Second-Opinion Packet** | Prepare the exact question and records for outside review |
| **Symptom Support** | Organize symptoms and determine the safest escalation using context and care-team instructions |
| **Insurance Appeal** | Organize a denial, evidence, deadline, and appeal draft |
| **Caregiver Handoff** | Transfer immediate logistics to another caregiver |
| **Survivorship** | Transition the same record into surveillance and late-effect tracking |

## Output modes

### Living Brief

The Living Brief stays intentionally short and answers:

- What should we do next?
- What do we know?
- What is still pending or uncertain?
- What should we ask next?

Example:

```text
Give me the current Living Brief with no more than three priority actions.
```

### Appointment Packet

Use before a clinical visit. It contains:

- purpose of the appointment
- what changed
- current treatment and disease context
- important pending information
- the decision likely to be discussed
- no more than five high-value questions
- useful records or facts to have available

### Decision Map

Use when there is a real choice to discuss. It separates:

- the decision being made
- realistic options
- why each might be considered
- evidence and major tradeoffs
- patient-specific constraints
- unknowns that could change the choice
- what the care team still needs to confirm

Cancer Care Companion explains the decision. It does not choose treatment for the patient.

### Biomarker Summary

For each relevant finding, preserve:

- biomarker or alteration
- result
- assay
- specimen
- date
- tissue versus blood
- somatic versus germline context
- supported clinical relevance
- remaining uncertainty

### Treatment Timeline

Track therapy chronologically, including modality, regimen or procedure, dates, line and intent when documented, response, toxicity, and reason for hold, stop, or change.

### Trial Shortlist

Clinical trial screening should normally return three to five candidates and include:

- NCT identifier
- intervention
- phase when applicable
- nearest relevant site
- site recruitment status
- why the study may be worth asking about
- obvious mismatch or uncertainty
- what the trial team must confirm

The repository includes a ClinicalTrials.gov API helper and an optional ChatGPT Action schema. Trial screening never establishes eligibility.

### Second-Opinion Packet

Match the review to the actual clinical question, such as pathology review, surgery, radiation, medical oncology, molecular tumor board, genetics, cellular therapy, transplant, or trial review.

### Caregiver Handoff

Provide only the immediate logistics another caregiver needs: treatment status, appointments, documented medication or treatment instructions, current watch items, contacts, unresolved tasks, and escalation instructions.

## The two-layer model

### 1. Patient-facing layer

A concise output that stays usable under stress.

### 2. Intelligence layer

A structured longitudinal cancer state that preserves:

- diagnosis and histology
- staging system, stage, and basis
- disease sites
- pathology
- biomarkers and molecular alterations
- germline findings
- treatments and treatment intent when documented
- response assessments
- symptoms and adverse effects
- pending studies
- appointments
- decision points
- candidate trials
- practical barriers
- source-document provenance
- contradictions and unresolved conflicts

A newer result never silently erases an older result.

## Evidence hierarchy

For current medical research, prefer:

1. national cancer agencies and official government sources
2. national regulators for approvals and labels
3. current official professional guidance when directly applicable
4. peer-reviewed primary evidence for unresolved or emerging questions
5. academic cancer-center pages for their own programs and trials
6. curated molecular resources only as supplemental evidence

Do not present search snippets, SEO health pages, social posts, or AI summaries as medical evidence.

## Symptom escalation

Cancer Care Companion does not use one universal oncology triage table for every patient. Escalation should consider:

- the oncology team's written instructions
- treatment type and timing
- immune suppression or other documented risk factors
- measured vital signs when available
- severity, duration, and progression
- ability to hydrate or take essential medication
- neurologic, respiratory, bleeding, allergic, or other emergency features

When urgent evaluation may be needed, the immediate action comes first and research does not delay it.

## Privacy

Use the privacy and data-handling rules of the environment in which Cancer Care Companion is running.

Do not place names, medical record numbers, dates of birth, exact addresses, insurance identifiers, or other direct identifiers into public web searches or clinical-trial API requests.

Do not put a real patient's private case record into reusable shared GPT Knowledge files or a shared Claude Skill package.

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

chatgpt/
  INSTRUCTIONS.md
  KNOWLEDGE_MANIFEST.md
  actions/
    clinicaltrials-openapi.yaml

scripts/
  package_claude_skill.py

.github/workflows/
  test.yml
  package-claude-skill.yml

CLAUDE_SKILL_INSTALL.md
CHATGPT_GPT_SETUP.md
QUICKSTART.md
claude-instructions.md
DISCLAIMER.md
LICENSE
```

## Installation summary

- **Claude Skill:** [`CLAUDE_SKILL_INSTALL.md`](./CLAUDE_SKILL_INSTALL.md)
- **ChatGPT Custom GPT:** [`CHATGPT_GPT_SETUP.md`](./CHATGPT_GPT_SETUP.md)
- **Claude Project:** [`claude-instructions.md`](./claude-instructions.md)
- **Practical usage:** [`QUICKSTART.md`](./QUICKSTART.md)

## Attribution

This project is inspired by and builds on concepts from [`petergyang/fuck-cancer`](https://github.com/petergyang/fuck-cancer), Copyright (c) 2026 Peter Yang, licensed under the MIT License.

## License

MIT. See `LICENSE`.
