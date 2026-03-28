# 🎯 AI Competitive Exam Trainer

A web app that helps you practice for GATE, CAT, SSB, and UPSC with AI examiners — powered by Google's Gemini AI. Built with a Streamlit UI, RAG for study material Q&A, and an Agent for real-time current affairs.

- Live Link -https://ai-competitive-exam-trainer-nk3tq5u4lddxjqyrgfvqzc.streamlit.app/
---

## What it does

Pick an exam and a topic, and an AI examiner starts asking you questions — progressively harder. It evaluates your answer, tells you what was good, what was missing, and gives you the ideal answer every time.

**Exams supported:**
- GATE CS/IT 💻 — MCQ questions on Data Structures, Algorithms, OS, Networks and more
- CAT/MBA 📊 — MCQ questions on Quant, Logical Reasoning, Verbal Ability
- SSB Interview 🎖️ — Written situational and behavioral questions
- UPSC Civil Services 🏛️ — Written questions on Polity, Ethics, Current Affairs

**Features:**
- Progressive difficulty — starts easy, gets harder
- Instant feedback after every answer
- Shows ideal answer that would score full marks
- Upload study material PDF and ask questions from it (RAG)
- Current affairs questions answered from real web data (Agent)
- Clean web interface

---

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/MansiRana3/AI-Exam-Trainer.git
cd AI-Exam-Trainer
```

**2. Create virtual environment**
```bash
py -m venv venv
.\venv\Scripts\Activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

Get Gemini key at [aistudio.google.com](https://aistudio.google.com)
Get Tavily key at [tavily.com](https://tavily.com)

**5. Run**
```bash
streamlit run app.py
```

---

## What I built under the hood

**RAG** — users can upload any study material PDF. The app chunks the document, stores embeddings in ChromaDB, searches by meaning when a question is asked, and sends relevant chunks to Gemini so it answers from the actual material.

**AI Agent** — for current affairs questions, the system automatically detects if web search is needed, searches using Tavily, and the examiner answers from real up-to-date results.

**Conversation memory** — the examiner remembers all previous questions and answers in the session so it can track your progress and increase difficulty appropriately.

**System prompts** — each examiner has a carefully crafted persona with specific rules, evaluation format, and behavior guidelines.

---

## Project structure
```
AI-Exam-Trainer/
├── .env                    # API keys — never committed
├── config.py               # All constants in one place
├── app.py                  # Streamlit web UI
├── rag.py                  # RAG - PDF loading and search
├── agent.py                # Agent - web search
├── personas/               # One file per exam type
│   ├── gate.py
│   ├── cat.py
│   ├── ssb.py
│   └── upsc.py
└── prompts/                # System prompt builder
```

---

## Things I want to add later

- Score tracking across sessions
- More exams — JEE, NEET, Banking
- Performance analytics dashboard
- Deploy online

---

## Tech used

Python, Google Gemini API (gemini-2.5-flash), google-genai SDK, Streamlit, ChromaDB, Tavily, pypdf, python-dotenv
```

