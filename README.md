# 🤖 AI Skill Assessment & Learning Plan Agent

## 📌 Overview

Resumes often tell what a candidate *claims* to know — not how well they actually know it.

This project builds an **AI-powered agent** that:

* Analyzes a Job Description (JD)
* Parses a candidate’s resume
* Evaluates real skill proficiency
* Identifies skill gaps
* Generates a **personalized learning roadmap**

---

## 🚀 Features

* 📄 Resume parsing (PDF support)
* 🧠 Skill extraction using LLM-style reasoning
* 🔍 JD vs Resume skill matching
* 💬 Conversational-style skill evaluation
* 📊 Skill scoring (0–5 scale)
* 📉 Gap analysis
* 📚 Personalized learning plan with timeline

---

## 🏗️ Architecture

``
User Input (JD + Resume)
        ↓
Skill Extraction (JD & Resume)
        ↓
Skill Matching Engine
        ↓
LLM-based Evaluator (or fallback layer)
        ↓
Scoring System
        ↓
Learning Plan Generator
        ↓
Streamlit UI Output
```

---

## ⚙️ Tech Stack

* Python
* Streamlit (UI)
* PyPDF2 (Resume parsing)
* LLM Integration (Gemini / fallback mock layer)

---

## 🧠 How It Works

1. Extracts skills from Job Description and Resume
2. Matches required vs existing skills
3. Evaluates proficiency using AI-generated questions
4. Assigns scores (0–5) per skill
5. Identifies missing/weak areas
6. Generates a realistic learning roadmap

---

## ▶️ Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

👉 [https://huggingface.co/spaces/Deepak-002/Skill-Assessment-AI-Agent]

---

## 📥 Sample Input

**Job Description:**

* Python, Machine Learning, SQL, Deep Learning

**Resume:**

* Python, Pandas, Basic ML

---

## 📤 Sample Output

| Skill            | Score |
| ---------------- | ----- |
| Python           | 4     |
| Machine Learning | 3     |
| Deep Learning    | 2     |
| SQL              | 2     |

### Missing Skills

* Deep Learning
* SQL

### Learning Plan

* Week 1–2: Python & Data Handling
* Week 3–4: Machine Learning
* Week 5–6: Deep Learning
* Week 7: SQL
* Week 8: Projects

---

## ⚠️ Limitations

* Dependent on LLM availability and quota
* Fallback mock layer used in low-quota scenarios
* Evaluation is simulated (not a real interview system)

---

## 🔮 Future Improvements

* Real-time interactive interview chatbot
* Advanced scoring using multiple signals
* Resume feedback suggestions
* Skill visualization (charts/radar graphs)
* Multi-role support

---

## 🎥 Demo Video

👉 

---

## 👨‍💻 Author

Deepak Sharma
