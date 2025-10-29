<h1 align="center">✨ QuillMate ✍️</h1>
<p align="center"><b>AI-Powered Creative Writing Assistant</b></p>
<p align="center"><i>Where Imagination Meets Innovation</i></p>

---

QuillMate is a full-stack AI application designed to support creative writers with intelligent content generation and refinement.  
Whether crafting stories, poems, or microfiction, QuillMate enhances creativity with real-time writing assistance powered by cutting-edge LLM technology.

---

## 🚀 Key Features

✅ **Idea Generator** — Create stories, poems, dialogues with customizable tone and genre  
✅ **Text Expansion** — Extend short passages while preserving writing style  
✅ **Tone & Style Analyzer** — Detect mood, complexity, and linguistic style  
✅ **Style Mimicry** — Recreate writing style from given samples  
✅ **Style Enhancer** — Improve fluency, clarity & overall readability  
✅ **PDF Export** — Download generated output instantly  

---

## 🧠 Tech Stack

| Category | Technology Used |
|---------|----------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Gradio |
| AI Model | Groq LLM API |
| Document Export | FPDF |

---

## 🏗 Architecture Overview
```
[ Gradio UI ]
│
│ User Input
▼
[ FastAPI Backend ]
│
▼ API Response / Display Output
[ Groq LLM Processing ]
│
▼
[ Optional PDF Export ]
```


A clean, modular system ensuring responsiveness and scalability.

---

## 📦 Installation & Usage

### Clone the Project
```bash
git clone https://github.com/Alfiya-Muhammed/QuillMate.git
cd QuillMate
Install Requirements
pip install -r requirements.txt

Start Backend
uvicorn main:app --reload

Run Gradio Interface
python app.py

🎯 How to Use

1️⃣ Enter prompt or upload sample text
2️⃣ Select writing mode, tone, and genre
3️⃣ Generate → Expand → Analyze → Enhance
4️⃣ Export final masterpiece as a PDF

Creativity + AI = ✨ Perfect Writing Experience
