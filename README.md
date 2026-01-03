# 📰 RAG-Based Financial News Chatbot

A **real-time Retrieval-Augmented Generation (RAG) application** that analyzes live financial news and answers stock market–related questions using the latest articles.

The chatbot fetches live RSS feeds, processes news articles, stores semantic embeddings, and uses an agent-based conversation flow for accurate, context-aware responses.

---

## 🔍 What This Project Does

- Fetches **live financial news** from trusted sources
- Converts news into **semantic embeddings**
- Retrieves relevant information using **vector similarity search**
- Generates **context-aware answers** using an LLM
- Maintains **conversation memory** across chats

---

## ✨ Features

- **Live RSS News Parsing**
  - Economic Times  
  - Times of India  
  - CNBC  
  - Google News (Stock Market – India)

- **RAG Pipeline**
  - Automatic text chunking
  - Vector embeddings for semantic search
  - News-grounded answers (no hallucinations)

- **LangGraph Agent**
  - Multi-step reasoning
  - Maintains last **10 messages** as context

- **Streaming Responses**
  - Real-time typing effect

- **Persistent Memory**
  - Chat history saved across sessions

- **Production Ready**
  - Handles **700+ news chunks**
  - Optimized retrieval using ChromaDB

---

## 🛠️ Tech Stack

- **Agent Orchestration**: LangGraph  
- **RAG Framework**: LangChain  
- **Embeddings**: HuggingFace Embeddings  
- **LLM**:
  - Gemini (API-based)
- **Data Sources**:
  - RSS Feeds → Article Extraction → Semantic Search

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python **3.10+**
- Git

---

### 📥 Clone Repository

```bash
git clone https://github.com/Gorisha2004/rag-news-chatbot-clean.git
cd rag-news-chatbot-clean
```
### 🧪 Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\Scripts\activate    # Windows
```
### 🔑 Environment Setup

Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_api_key_here
```
Get your API key from:
👉 https://ai.google.dev

### Run the Application
python main.py

### 📁 Project Structure
rag-news-chatbot/
├── main.py                     # Application entry point
├── conversation_graph.py       # LangGraph agent logic
├── embedder.py                 # Vector store & embeddings
├── data_fetcher.py             # RSS feed collection
├── article_extractor.py        # Article parsing
├── chunker.py                  # Text chunking
├── retriever.py                # Semantic search
├── chat_history_manager.py     # Conversation memory
├── .env                        # API keys (ignored)
├── .gitignore                  # Prevents secret commits

### 📦 Dependencies
pip install langchain langgraph langchain-community
pip install langchain-huggingface
pip install sentence-transformers torch
pip install newspaper3k feedparser python-dotenv
pip install lxml_html_clean

