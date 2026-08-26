# Install Cancer Care Companion as a Custom GPT in ChatGPT

Cancer Care Companion can be configured as a dedicated **Custom GPT** in ChatGPT. This is separate from the Claude Skill and Claude Project installation paths.

> **Current ChatGPT availability:** OpenAI currently limits creation and publishing of new GPTs to eligible Business, Enterprise, and Edu workspaces, subject to workspace permissions. Existing GPTs may still be editable where permitted. If your account does not show **Create** in the GPTs area, use the same Cancer Care Companion instructions in a ChatGPT Project instead.

Official OpenAI setup documentation: https://help.openai.com/en/articles/8554397

## 1. Create the GPT

On the ChatGPT web app:

1. Open **GPTs** / **Explore GPTs**.
2. Select **Create**.
3. Open the configuration view.
4. Use the fields below.

### Name

```text
Cancer Care Companion
```

### Description

```text
A longitudinal cancer-navigation companion for patients and caregivers. Organizes reports, tracks what is confirmed or pending, prepares appointments and decisions, explains biomarkers, screens trials, and coordinates practical care without replacing the oncology team.
```

### Instructions

Copy the full contents of:

```text
chatgpt/INSTRUCTIONS.md
```

into the GPT **Instructions** field.

Do not use Knowledge files as a substitute for these instructions. The Instructions field defines behavior; Knowledge files provide supporting reference material.

## 2. Add conversation starters

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

## 3. Upload Knowledge files

Open the GPT's **Knowledge** section and upload the files listed in:

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
DISCLAIMER.md
```

These files support structure and reference behavior. The active case itself should normally be supplied by the user in the conversation or through the workspace in which the GPT is being used.

## 4. Enable capabilities

Recommended capabilities:

| Capability | Setting | Why |
| --- | --- | --- |
| **Web search** | On | Current evidence, official cancer sources, drug approvals, guidance, trial verification, cancer-center information |
| **Code Interpreter & Data Analysis** | On | Structured report extraction, timelines, tables, uploaded files, simple calculations |
| **Image generation** | Optional | Not required for the core cancer-navigation workflow |

When current medical information is needed, the GPT should favor official cancer agencies, regulators, professional guidance, peer-reviewed literature, ClinicalTrials.gov, and official cancer-center sources.

## 5. Optional: add a ClinicalTrials.gov Action

For more deterministic trial discovery, an optional OpenAPI schema is included at:

```text
chatgpt/actions/clinicaltrials-openapi.yaml
```

In the GPT editor, add an **Action**, import that schema, and configure it with **no authentication**. It calls the public ClinicalTrials.gov API v2.

This Action is optional. Web search can still be used when Actions are unavailable.

Important boundaries remain the same:

- treat API results as candidate trials, not proof of eligibility
- verify overall study status and the specific site's recruitment status
- inspect full eligibility criteria before presenting a trial as plausible
- do not place names, medical record numbers, dates of birth, or other direct identifiers in trial-search parameters

## 6. Test in Preview

Before sharing the GPT, test at least these scenarios:

1. **New diagnosis with incomplete staging**
   - It should create a useful partial record without pretending missing information is negative.

2. **New pathology contradicts an older report**
   - It should preserve both and flag the conflict rather than silently overwrite the older result.

3. **New molecular report**
   - It should preserve alteration, assay, specimen, date, and whether the relevance is actually supported.

4. **Treatment decision**
   - It should explain realistic options and tradeoffs without choosing treatment for the patient.

5. **Clinical trial request**
   - It should return a small shortlist and clearly state that the trial team must confirm eligibility.

6. **Potentially urgent symptom**
   - It should put the safest immediate action first and not let research delay urgent evaluation.

7. **Routine update**
   - It should update the existing longitudinal case rather than starting a second tracker.

## 7. Recommended usage pattern

For a new case:

```text
I want to use Cancer Care Companion for my mother's case. Read these reports, build the longitudinal cancer state, then give me the Living Brief with the three most important next actions.
```

For later updates:

```text
Update the existing case with this new pathology report. Preserve the previous findings, identify what changed, and regenerate the Living Brief.
```

For an appointment:

```text
Create an Appointment Packet for Friday. Focus on the decision we need to make, pending information, and no more than five high-value questions.
```

For a decision:

```text
Create a Decision Map for the options the oncologist discussed. Show why each might be considered, major tradeoffs, evidence, and what still needs confirmation.
```

## 8. Sharing

If your workspace allows sharing or publishing GPTs, test the GPT with de-identified synthetic cases before wider release. Do not embed a real patient's private record into the GPT's shared Knowledge files.

## ChatGPT Project fallback

If Custom GPT creation is not available on your account, create a ChatGPT Project and place `chatgpt/INSTRUCTIONS.md` in the project's instructions. Upload the same Knowledge files and keep the patient's ongoing documents and conversations in that Project.

The functionality is similar, but the Custom GPT is the reusable product-style experience while a Project is better suited to one long-running case.
