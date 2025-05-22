## ATS NER Competition Instructions

Welcome to the ATS (Applicant Tracking System) NER competition! Participants will form teams of **two** and follow the four phases below.

---

### 📋 Setup

1. **Form Teams**: Two participants per team.
2. **Dataset**: Download the resume dataset from Kaggle: [https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)
3. **Doccano Project**:

   * Create a new project in Doccano with **Sequence Labeling**.
   * Import the provided `labels.json` (8 entity tags) via **Labels → Import**.

---

### 🚀 Phase 1: Annotation (30 minutes)

* **Objective**: Split the dataset, label as many resumes as possible, and export your annotations.
* **Steps**:

  1. In your Doccano project, upload half of the dataset for your team.
  2. Annotate the resumes using these entity tags:

     ```json
     [
       {"text":"PERSON_NAME"},
       {"text":"EMAIL"},
       {"text":"PHONE"},
       {"text":"DEGREE"},
       {"text":"UNIVERSITY"},
       {"text":"JOB_TITLE"},
       {"text":"COMPANY"},
       {"text":"SKILL"}
     ]
     ```
  3. Export your annotated data in JSONL format when time is up.

> ⏱ **Time limit**: 1 hour

---

### 🤖 Phase 2: Model Training & Hub Upload (30 minutes)

* **Objective**: Fine-tune a spaCy NER model on your labeled data and publish it.
* **Steps**:

  1. Open Google Colab and install spaCy: `!pip install spacy`
  2. Convert your JSONL annotations into spaCy training format.
  3. Train a basic NER pipeline on your exported data.
  4. Save the trained model as a package and upload it to the Hugging Face Hub under your team name.

> ⏱ **Time limit**: 30 minutes

---

### 🖥️ Phase 3: UI, Docker & Deployment (45 minutes)

* **Objective**: Build a simple web UI for your NER service, containerize it, and deploy.
* **Steps**:

  1. Create a minimal web interface wit Streamlit that accepts resume text and highlights named entities.
  2. Write a `Dockerfile` to containerize your app and your spaCy model.
  3. Deploy your Docker container to **Hamravesh**.

> ⏱ **Time limit**: 45 minutes

---

### 💬 Phase 4: Community Engagement (15 minutes)

* **Objective**: Showcase your application and give feedback to peers.
* **Steps**:

  1. Post a brief demo of your deployed application (screenshots or link) in the competition forum.
  2. Comment on at least two other teams’ posts with constructive feedback.

> ⏱ **Time limit**: 15 minutes

---

Good luck to all teams—may the best ATS NER demo win!
