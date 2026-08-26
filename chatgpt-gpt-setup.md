# Cancer Care Companion as a Custom GPT in ChatGPT

Use this setup when you want Cancer Care Companion configured as a dedicated **Custom GPT** in ChatGPT.

This remains separate from the Claude Skill, Claude Project, and ChatGPT Work options in the repository.

> **Current ChatGPT availability:** OpenAI currently limits creation and publishing of new GPTs to eligible Business, Enterprise, and Edu workspaces, subject to workspace permissions. Existing GPTs may still be editable where permitted. If your account does not show **Create** in the GPTs area, use the same Cancer Care Companion instructions in a ChatGPT Project or use `chatgpt-work-instructions.md` for artifact-oriented work.

Official OpenAI documentation: https://help.openai.com/en/articles/8554397

## 1. Create the GPT

On the ChatGPT web app:

1. Open **GPTs** / **Explore GPTs**.
2. Select **Create**.
3. Open the configuration view.
4. Use the configuration below.

### Name

```text
Cancer Care Companion
```

### Description

```text
A longitudinal cancer-navigation companion for patients and caregivers. Organizes reports, tracks what is confirmed or pending, prepares appointments and decisions, explains biomarkers, screens trials, and coordinates practical care without replacing the oncology team.
```

## 2. Add the GPT Instructions

Copy the full contents of:

```text
chatgpt/INSTRUCTIONS.md
```

into the GPT **Instructions** field.

The Instructions field is the behavioral layer. It contains the longitudinal case workflow, fact states, decision support rules, trial boundaries, symptom handling, evidence hierarchy, privacy rules, and output modes.

Do not use Knowledge files as a substitute for the Instructions field.

## 3. Add conversation starters

Use these conversation starters:

```text
Build a living cancer record from these reports and tell me the three things that matter most now.
```

```text
Prepare me for my next oncology appointment using the information in this case.
```

```text
Create a decision map for the treatment options my oncologist discussed.
```

```text
Explain these pathology and biomarker results in plain English and show what they may affect.
```

```text
Find candidate clinical trials near me and explain what the trial team would still need to confirm.
```

```text
Update the case with this new scan and show exactly what changed.
```

## 4. Upload Knowledge files

Use the file list in:

```text
chatgpt/KNOWLEDGE_MANIFEST.md
```

Recommended core Knowledge files are:

```text
schemas/cancer-state.schema.json
templates/living-brief.md
templates/appointment-packet.md
templates/decision-map.md
QUICKSTART.md
skills/cancer-care-companion/eval.md
DISCLAIMER.md
```

These files provide reusable structure and reference material.

Do **not** put a real patient's private record into the GPT's shared Knowledge files. Patient-specific pathology, imaging, molecular reports, notes, and other case material should be supplied by the user within the appropriate private conversation or workspace according to the account's privacy rules.

## 5. Enable capabilities

Recommended capabilities:

| Capability | Setting | Why |
| --- | --- | --- |
| **Web search** | On | Current evidence, drug approvals, professional guidance, trial verification, and cancer-center information |
| **Code Interpreter & Data Analysis** | On | Uploaded-report analysis, structured timelines, tables, case-state files, and calculations |
| **Image generation** | Optional | Not required for the core workflow |

When current medical information is needed, the GPT should favor official cancer agencies, regulators, professional guidance, peer-reviewed literature, ClinicalTrials.gov, and official cancer-center sources.

## 6. Optional ClinicalTrials.gov Action

For more deterministic clinical-trial discovery, the repository includes an optional OpenAPI Action schema:

```text
chatgpt/actions/clinicaltrials-openapi.yaml
```

In the GPT editor:

1. Add an **Action**.
2. Import the OpenAPI schema.
3. Configure it with **no authentication**.
4. Test it with a synthetic, non-identifying cancer query.

The Action calls the public ClinicalTrials.gov API v2.

The Action is optional. Web search can still be used when Actions are unavailable.

Trial-search boundaries:

- treat results as candidate studies, not proof of eligibility
- verify overall study status and the relevant site's recruitment status
- inspect eligibility criteria before calling a study a plausible match
- do not put names, medical record numbers, dates of birth, addresses, or other direct identifiers into Action parameters

## 7. Test the GPT in Preview

Before sharing it, test at least these scenarios.

### New diagnosis with incomplete staging

The GPT should create a useful partial case without converting missing information into negative findings.

### New pathology contradicts an older report

The GPT should preserve both findings, dates, and sources and flag the conflict rather than silently overwrite the older result.

### New molecular report

The GPT should preserve alteration, assay, specimen, date, and somatic or germline context and should not infer actionability from a gene name alone.

### Treatment decision

The GPT should explain realistic options, evidence context, and tradeoffs without choosing treatment for the patient.

### Clinical trial request

The GPT should return a small shortlist and clearly state what the trial team still needs to confirm.

### Potentially urgent symptom

The safest immediate action should appear first. Research must not delay urgent evaluation.

### Routine update

The GPT should update the existing longitudinal case rather than start a second tracker.

## 8. Recommended usage pattern

### New case

```text
I want to use Cancer Care Companion for my mother's case. Read these reports, build the longitudinal cancer state, then give me the Living Brief with the three most important next actions.
```

### New report

```text
Update the existing case with this new pathology report. Preserve the previous findings, identify what changed, and regenerate the Living Brief.
```

### Appointment

```text
Create an Appointment Packet for Friday. Focus on the decision we need to make, pending information, and no more than five high-value questions.
```

### Decision

```text
Create a Decision Map for the options the oncologist discussed. Show why each might be considered, major tradeoffs, evidence, and what still needs confirmation.
```

## 9. Sharing

If your workspace allows sharing or publishing GPTs, test the GPT with de-identified synthetic cases before wider release.

The reusable GPT should contain the Cancer Care Companion behavior and reference material, not a particular patient's private case record.

## ChatGPT Project fallback

If Custom GPT creation is unavailable, create a ChatGPT Project and place `chatgpt/INSTRUCTIONS.md` in the Project instructions. Upload the same Knowledge files and keep the patient's ongoing case materials in that Project.

The Custom GPT is the reusable product-style experience. A Project is better suited to one long-running private case.
