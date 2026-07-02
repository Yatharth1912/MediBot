# 🩺 MediBot - Healthcare Triage Assistant

A rule-based chatbot that helps users understand their symptoms, assesses severity, and recommends appropriate medical specialists.

## 🎯 Problem It Solves

Most people Google their symptoms and end up either panicking or ignoring warning signs. MediBot provides structured, rule-based symptom analysis without the noise.

## ✨ Features

- **Symptom Recognition** — Understands natural language symptom descriptions
- **Severity Scoring** — Classifies conditions as Low, Moderate, or High priority
- **Emergency Detection** — Instantly flags critical symptoms
- **Specialist Recommendation** — Suggests which doctor to consult
- **Conversation Memory** — Tracks context across messages

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit (UI)
- Regex & Pattern Matching (NLP)
- JSON (Knowledge Base)

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/MediBot.git
cd MediBot

# Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py