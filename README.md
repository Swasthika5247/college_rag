# 🎓 College RAG Assistant

[NOTE: Desigined based on KSRCE curriculum]
A Retrieval-Augmented Generation (RAG) application that answers questions about a college curriculum PDF using semantic search and a Large Language Model.

Instead of relying solely on the LLM's knowledge, the application retrieves the most relevant sections from the uploaded curriculum document using FAISS and Sentence Transformers, then generates accurate, context-aware responses using Groq's Llama 3.3 model.

---

## 🚀 Features

- 📄 Load and process college curriculum PDFs
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🔍 Store embeddings in a FAISS vector database
- 💬 Answer natural language questions using Groq Llama 3.3
- ⚡ Fast semantic search with Retrieval-Augmented Generation (RAG)

---

## 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face
- Groq API
- Llama 3.3 70B Versatile

---

## 📂 Project Structure

```
college_rag/
│
├── app.py                  # Terminal chatbot
├── data/                   # PDF documents
├── src/
│   ├── data_loader.py
│   ├── embedding.py
│   ├── vectorstore.py
│   └── search.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/college-rag.git
cd college-rag
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run

```bash
python app.py
```

---

## 💡 Example Questions

- What are the subjects in Semester 3?
- What are the objectives of Professional Communication?
- Which subjects have 2 credits?
- Summarize the Operating Systems syllabus.
- Which semester contains Artificial Intelligence?
- What are the laboratory courses?

---

## 🧠 How It Works

1. Load curriculum PDF
2. Split into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant chunks based on the user's query
6. Send retrieved context to Groq Llama 3.3
7. Generate an answer grounded in the retrieved documents

---

## 📈 Future Improvements

- Streamlit web interface
- Multiple PDF support
- Citation support
- Hybrid search (keyword + semantic)
- Conversation memory
- Document upload from UI

---

## 👨‍💻 Author

**Swasthika V**
