
# SummaryIO 🚀

**SummaryIO** is a Python-based web and YouTube content summarizer built with **LangChain** and Meta’s **meta-llama/llama-4-scout-17b-16e-instruct** model via **GROQ**.  
It allows users to quickly summarize long-form content from websites and YouTube videos.

---

## 🧠 Features

- 🌐 Website URL summarization  
- ▶️ YouTube video transcript summarization  
- 🦙 Meta LLaMA 4 Scout 17B Instruct model  
- 🔗 LangChain-based pipeline  
- 🐍 Conda environment support  

---

## 📁 Project Structure

```
SummaryIO/
├── README.md
├── app.py
├── requirements.txt
└── .gitignore
```

---

## 🧰 Tech Stack

- Python
- LangChain
- GROQ
- Meta LLaMA 4 Scout 17B Instruct
- Conda

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Tridib2510/SummaryIO.git
cd SummaryIO
```

### 2️⃣ Create Conda Environment

```bash
conda create -n summaryio python=3.10
conda activate summaryio
pip install -r requirements.txt
```

## ▶️ Usage

### Website Summarization

```bash
python main.py --url "https://example.com"
```

### YouTube Summarization

```bash
python main.py --youtube "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## 📌 Output Example

```
• Key insights
• Important takeaways
• Concise explanation
```

---

## 📦 Deployment

Can be deployed as:
- Streamlit App

## 📜 License

MIT License

---

## 🙌 Author

**Tridib**  
GitHub: https://github.com/Tridib2510
