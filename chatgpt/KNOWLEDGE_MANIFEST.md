# ChatGPT Custom GPT Knowledge Manifest

Use the GPT **Instructions** field for behavior and workflow rules. Use **Knowledge** for reusable reference material.

## Upload these files

### Required

1. `schemas/cancer-state.schema.json`
   - Defines the structured longitudinal cancer state.

2. `templates/living-brief.md`
   - Defines the concise patient/caregiver summary format.

3. `templates/appointment-packet.md`
   - Defines the visit-preparation output.

4. `templates/decision-map.md`
   - Defines the treatment or care decision comparison output.

5. `DISCLAIMER.md`
   - Defines the project-level medical and privacy boundaries.

### Recommended

6. `QUICKSTART.md`
   - Gives practical usage examples and expected workflows.

7. `skills/cancer-care-companion/eval.md`
   - Provides the quality checklist used to evaluate outputs.

## Do not upload a real patient's record as shared GPT Knowledge

The GPT Knowledge area is for reusable product reference material. A patient's pathology, imaging, molecular reports, notes, insurance documents, and other private case information should be supplied within the user's own conversation or case workspace according to the privacy rules of the account being used.

## Why `SKILL.md` is not required as Knowledge

The core behavioral instructions have already been adapted into `chatgpt/INSTRUCTIONS.md` for the Custom GPT's **Instructions** field. OpenAI recommends placing behavior and workflow rules in Instructions and using Knowledge for reference material.

Uploading `SKILL.md` as Knowledge is optional, but it should not replace `chatgpt/INSTRUCTIONS.md`.
