# SummaryIO

**SummaryIO** is a Python-based YouTube and Website content summarizer that extracts high-quality, concise summaries from URLs — whether it’s a YouTube video or any public article/webpage.

It uses **LangChain**, the **meta-llama/llama-4-scout-17b-16e-instruct** model through the **Groq API**, and the **uv package manager** for fast, lightweight dependency handling.

---

## 🚀 Features

* 📺 **YouTube Video Summarization:** Accept a YouTube link and generate a clear, structured summary of the spoken content.
* 🌐 **Website Summarization:** Generate a summary from any public article or blog post by its URL.
* 🤖 **LLM Powered:** Uses the Meta LLaMA 17B-instruction model for consistent, high-quality output.
* 📦 **Simple CLI Interface:** Run summarization with a single command using `main.py` or via an API wrapper (`app.py`).

---

## 🧱 Project Structure

```
SummaryIO/
├── .python-version
├── README.md
├── app.py
├── main.py
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

* `main.py`: Main CLI script that handles YouTube or website summarization.
* `app.py`: Optional API server entrypoint if you want to wrap SummaryIO in a web service.
* `requirements.txt`: Python dependency list.
* `pyproject.toml` & `uv.lock`: Project metadata & dependency lock files.

---

## 🛠️ Installation

1. **Clone the project**

```bash
git clone https://github.com/Tridib2510/SummaryIO.git
cd SummaryIO
```

2. **Install dependencies**

Using **uv**:

```bash
uv install
```

Or with **pip**:

```bash
pip install -r requirements.txt
```

3. **Set Groq API Key**

```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

For Windows:

```powershell
setx GROQ_API_KEY "your_groq_api_key_here"
```

---

## ▶️ Usage

**YouTube Summarization:**

```bash
python main.py --youtube https://www.youtube.com/watch?v=<VIDEO_ID>
```

**Website Summarization:**

```bash
python main.py --url https://example.com/article
```

---

## 🧠 How It Works

1. Extracts text or transcript from the provided URL.
2. Processes content through a LangChain summarization chain.
3. Generates a human-readable summary using the Groq API LLaMA model.

---

## 🧪 Example Output

**YouTube:** Summarized key concepts into concise bullets.

**Website Article:** Summarized a long article into a clear 3-paragraph summary.

---

## 🧩 Optional API Server

```bash
python app.py
```

Then send POST requests to:

```bash
http://localhost:8000/summarize
```

With JSON body:

```json
{"url": "https://example.com/article"}
```

Returns structured summary in JSON.

---

## 💡 Tips

* Network access is required for URLs.
* YouTube transcripts must be available (auto-generated or manual).

---

## 👥 Contributing

1. Fork it
2. Create a branch (`git checkout -b feature-name`)
3. Code enhancements
4. Push & open a Pull Request

---

## 📜 License

MIT License.

---

## 📬 Contact

* GitHub: [https://github.com/Tridib2510](https://github.com/Tridib2510)
* Project: [https://github.com/Tridib2510/SummaryIO](https://github.com/Tridib2510/SummaryIO)

---

✨ *Enjoy fast, accurate summarization with SummaryIO!* 🚀
