# Cancer Care Companion Quick Start

This guide is for patients and caregivers who want to use Cancer Care Companion without reading the technical architecture first.

## 1. Install or load the skill

### Agent Skills CLI

```bash
npx skills add DataDrivenMed/cancer-care-companion --skill cancer-care-companion --global --yes
```

If you are testing the `comprehensive-v2` branch before it is merged:

```bash
git clone -b comprehensive-v2 https://github.com/DataDrivenMed/cancer-care-companion.git
npx skills add ./cancer-care-companion --skill cancer-care-companion --global --yes
```

### Claude Project

Copy `claude-instructions.md` into the Project Instructions and use that project for the same case over time.

### Other persistent AI workspaces

Use `skills/cancer-care-companion/SKILL.md` as the persistent instructions.

## 2. Start the case

You do not need complete records.

Use one of these patterns.

### Brain dump

```text
/cancer-care My dad was diagnosed with colorectal cancer. We have a biopsy report and CT scan. We meet medical oncology next week. Build the initial living record and tell me the three things that matter most now.
```

### Uploaded records

```text
/cancer-care Read the uploaded pathology, imaging, and oncology notes. Create the longitudinal cancer record. Separate confirmed facts, pending results, uncertainty, and conflicting information. Then create the living brief.
```

### Existing cancer brief

```text
/cancer-care Use this existing cancer brief as the starting source of truth. Preserve the concise summary but build the deeper longitudinal record behind it.
```

## 3. Keep one evolving case

The main benefit comes from updating the same record rather than starting over.

When a new report arrives:

```text
/cancer-care update Add this report to the existing case. Tell me what changed, what stayed the same, and whether the next decision changes.
```

When you receive several documents at once:

```text
/cancer-care update Add all of these documents. Reconcile dates and duplicate findings. Keep contradictions visible instead of silently selecting one version.
```

## 4. Ask for the view you need

### I need the shortest summary

```text
/cancer-care brief Give me the current one-page living brief.
```

### We have an appointment tomorrow

```text
/cancer-care appointment Prepare an appointment packet for tomorrow's oncology visit. Include what changed, pending results, the likely decision point, and the five highest-value questions.
```

### We have to make a treatment decision

```text
/cancer-care decision Compare the options the oncologist discussed. Show why each might be considered, important tradeoffs, evidence, patient-specific constraints, and what still needs confirmation. Do not choose for us.
```

### We received a molecular or pathology report

```text
/cancer-care biomarkers Add this report to the existing case. Explain every important result in context and show specimen, assay, date, result, potential significance, and uncertainty.
```

### I cannot remember the treatment history

```text
/cancer-care treatment Reconstruct the treatment timeline from the records. Include treatment intent, regimen or procedure, dates, response, toxicity, and reason for stopping or changing when documented.
```

### We want to explore clinical trials

```text
/cancer-care trials Find three to five candidate trials within 150 miles that fit the confirmed cancer type, biomarker, stage, and treatment setting. Check the individual site's recruitment status and list what the trial team still needs to confirm.
```

### We want a second opinion

```text
/cancer-care second-opinion Based on the current decision, tell me what type of second opinion is most useful and create a concise packet with the exact question we want reviewed.
```

### A new symptom appeared

```text
/cancer-care symptoms She developed a new fever and chills after treatment. Use the care-team instructions and treatment context already in the record. Tell me the safest next action first.
```

If the symptom appears life-threatening, seek emergency help rather than waiting for the tool.

### Insurance denied something

```text
/cancer-care appeal Organize this denial into an appeal packet. Separate the denial reason, deadline, evidence needed, supporting medical rationale, and questions for the oncology office and insurer.
```

### Another caregiver is taking over

```text
/cancer-care caregiver My brother is covering care for the next week. Create a handoff with only the appointments, pending tasks, treatment logistics, contact needs, and watch items he needs.
```

## 5. Suggested workflow around an oncology visit

### Two or three days before

```text
/cancer-care appointment Prepare us for the visit based on everything in the current record.
```

### Immediately after

Paste your notes or upload the visit summary:

```text
/cancer-care update Add today's oncology visit. Record the recommendation, what was decided, what remains undecided, new orders, pending tests, and next milestone.
```

### If the visit created a major choice

```text
/cancer-care decision Build a decision map for the options discussed today.
```

## 6. Suggested workflow when a new scan arrives

```text
/cancer-care update Add this scan. Compare it with the most relevant prior imaging. Update disease sites and documented response. Separate radiology findings from conclusions that require the oncology team.
```

Then, if it changes the treatment question:

```text
/cancer-care decision Does this scan create a new decision point? If yes, map it.
```

## 7. Suggested workflow when molecular testing arrives

```text
/cancer-care biomarkers Add this molecular report to the case. Compare it with prior tissue or liquid-biopsy testing. Flag discordant findings and distinguish established clinical relevance from uncertain or emerging evidence.
```

Then:

```text
/cancer-care appointment Create the questions we should ask the oncologist about these molecular findings.
```

## 8. What the tool should remember

For the same case, the system should maintain or reconstruct:

- diagnosis and histology
- stage and staging basis
- disease sites
- pathology findings
- biomarkers and molecular results
- germline testing
- treatment history
- response assessments
- important toxicities and symptoms
- pending tests and appointments
- unresolved decisions
- trial candidates
- practical barriers
- source documents
- conflicting information

A newer report should not silently erase an older one.

## 9. What not to ask it to do

Cancer Care Companion is designed to organize, explain, research, and prepare questions. It should not:

- diagnose cancer from incomplete information
- prescribe treatment
- decide which treatment you should receive
- claim that a patient qualifies for a clinical trial
- replace emergency evaluation
- silently resolve contradictory medical records

## 10. The simplest possible way to use it

If you remember nothing else, use these four prompts repeatedly:

```text
/cancer-care update Add this new information to our existing case and tell me what changed.
```

```text
/cancer-care brief What are the three things that matter most right now?
```

```text
/cancer-care appointment Prepare us for the next appointment.
```

```text
/cancer-care decision What decision are we facing, what are the options, and what do we still need to know?
```

That is the core Cancer Care Companion workflow.
