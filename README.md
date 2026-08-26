# Cancer Care Companion

> **A downstream AI companion skill for cancer patients and caregivers.** 
> Built to work alongside open-source care navigation tools like [Peter Yang's /fuck-cancer](https://github.com/petergyang/fuck-cancer).

## 🤔 What is this?
Tools like `/fuck-cancer` are incredible at gathering medical intelligence, finding clinical trials, and building a master "War Room" brief. 

**The Cancer Care Companion** takes that data a step further. It translates complex medical briefs into daily survival guides, triages emergency symptoms, drafts insurance appeal letters, and handles clinical trial travel logistics.

---

## ⚡ The Unified Command System
This skill uses a single command label: **`/cancer-care`**. 
Simply type the command followed by your category and context in your LLM.

| Command | What it does | Example |
| :--- | :--- | :--- |
| `/cancer-care split` | Splits a medical brief into a **Patient View** (daily life, empathy) and a **Caregiver View** (logistics, billing, trials). | `/cancer-care split [paste your brief here]` |
| `/cancer-care triage` | Instantly checks symptoms against oncology "Red Flags" (e.g., neutropenic fever) and tells you if you need the ER. | `/cancer-care triage My dad has a 101.2 fever and chills` |
| `/cancer-care appeal` | Drafts a formal insurance appeal letter for denied treatments or scans, citing standard-of-care guidelines. | `/cancer-care appeal Insurance denied the PET scan` |
| `/cancer-care trials` | Provides travel logistics, lodging resources (Joe's House, Angel Flight), and insurance questions for out-of-state clinical trials. | `/cancer-care trials Trial is at MD Anderson, we live in Ohio` |
| `/cancer-care explain` | Translates complex lab values into plain English and explains how they affect daily life (e.g., diet, safety). | `/cancer-care explain Absolute Neutrophil Count` |

---

## 🚀 How to Install This Skill

### 🟠 In Claude (Projects)
1. Go to [Claude.ai](https://claude.ai) and create a new **Project**.
2. Open **Project Instructions**.
3. Copy and paste the contents of [`claude-instructions.md`](./claude-instructions.md) into the box.
4. *(Optional but recommended)* Upload oncology triage guidelines to the Project Knowledge.

### 🟢 In ChatGPT (Custom GPTs)
1. Go to **My GPTs** -> **Create a GPT**.
2. Name it **Cancer Care Companion**.
3. Paste the contents of [`chatgpt-gpt-setup.md`](./chatgpt-gpt-setup.md) into the **Instructions** box.
4. Add the conversation starters provided in the file.

### 🔵 In Gemini (Gems)
1. Go to [gemini.google.com](https://gemini.google.com) and click **Gem manager**.
2. Click **Create new Gem**.
3. Paste the contents of [`gemini-gem-setup.md`](./gemini-gem-setup.md) into the instructions.

---

## ⚠️ Medical & Privacy Disclaimer
This tool is an AI assistant, **NOT a doctor**. It does not diagnose or prescribe. Always verify medical decisions with your oncology care team. 

**HIPAA Warning:** Never upload real names, dates of birth, or exact addresses to public AI tools. Always anonymize data (e.g., use "Patient X", "Age 65", "City A").

---

## 🙏 Credits
*   Inspired by and designed to complement [Peter Yang's /fuck-cancer](https://github.com/petergyang/fuck-cancer) open-source skill.
*   Built for the caregiver community.
