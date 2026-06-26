# 🤖 RAG Q&A Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using:

- LangChain
- ChromaDB
- HuggingFace Embeddings
- OpenRouter
- Streamlit

## Features

- Semantic search using vector embeddings
- Context-aware question answering
- Free LLM integration via OpenRouter
- Interactive Streamlit UI

## Project Structure

```text
RAG-QNA-CHATBOT/
├── data/
├── src/
│   ├── ingest.py
│   ├── rag.py
│   ├── app.py
│   └── test_rag.py
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd RAG-QNA-CHATBOT

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Running the Application

Create embeddings:

```bash
python src/ingest.py
```

Start the UI:

```bash
streamlit run src/app.py
```

## Architecture

```text
Documents
   ↓
Text Loader
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Retriever
   ↓
LLM (OpenRouter)
   ↓
Answer
```