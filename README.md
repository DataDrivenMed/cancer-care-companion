# Cancer Care Companion

> A longitudinal, evidence-grounded cancer navigation skill for patients and caregivers.

Cancer Care Companion builds on the concise patient-advocacy brief concept in [Peter Yang's `/fuck-cancer`](https://github.com/petergyang/fuck-cancer) and expands it into a modular cancer-navigation system.

The design goal is simple: **keep the patient-facing output short while making the intelligence behind it much deeper.**

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

## Unified command

Use `/cancer-care` with natural language. Subcommands are optional convenience shortcuts rather than separate products.

```text
/cancer-care Update our living brief with this pathology report.
/cancer-care appointment Prepare us for Friday's oncology visit.
/cancer-care decision Compare the options the oncologist discussed.
/cancer-care biomarkers Explain these molecular results and what they may affect.
/cancer-care trials Find candidate trials within 150 miles.
/cancer-care second-opinion What type of second opinion would be most useful now?
/cancer-care symptoms She has a new fever and chills after treatment. What should we do?
/cancer-care appeal Help organize an appeal for this denial.
/cancer-care caregiver Create a handoff for my brother who is covering this week.
```

## Output modes

The same underlying record can generate:

- **Living Brief**: shortest patient/caregiver summary
- **Appointment Packet**: visit preparation and questions
- **Decision Map**: options, evidence, tradeoffs, and unknowns
- **Trial Shortlist**: three to five candidate studies with site status
- **Second-Opinion Packet**: concise case summary plus exact review question
- **Treatment Timeline**: chronological therapy, response, and toxicity history
- **Biomarker Summary**: molecular findings with specimen, assay, date, and provenance
- **Caregiver Handoff**: immediate logistics and watch items

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
schemas/
  cancer-state.schema.json
templates/
  living-brief.md
  appointment-packet.md
  decision-map.md
claude-instructions.md
DISCLAIMER.md
LICENSE
```

## Status

`comprehensive-v2` is the expanded architecture. Initial implementation focuses on the longitudinal state model, safer symptom handling, patient/caregiver views, decision support, evidence provenance, and reusable output templates.

## Attribution

This project is inspired by and builds on concepts from [`petergyang/fuck-cancer`](https://github.com/petergyang/fuck-cancer), Copyright (c) 2026 Peter Yang, licensed under the MIT License.

## License

MIT. See `LICENSE`.
