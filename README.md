# 🚀 RAG News Chatbot - Live Financial News Analysis

Real-time **stock market chatbot** that answers questions using **latest RSS news** from Economic Times, Times of India, CNBC + Google News. Built with **LangGraph agent** + **RAG pipeline** for production-grade conversations.

## ✨ Features
- **Live RSS parsing** → Economic Times, TOI, CNBC, Stock Market India
- **LangGraph conversation agent** with memory (10 message context)
- **Automatic chunking** + **vector embeddings** for semantic search
- **Streaming responses** (real-time typing effect)
- **Persistent memory** across conversations
- **Production ready** (handles 700+ news chunks)


## 🛠️ Tech Stack
LangGraph (agent orchestration) + LangChain (RAG)
HuggingFace Embeddings (free unlimited)
Gemini LLM / Ollama (local)
Chroma Vector DB (persistent cache)
RSS feeds → Article extraction → Semantic search


## 🚀 Quick Setup (5 min)

### Prerequisites
- Python 3.10+
- Git

### 1. Clone & Install
```bash
git clone https://github.com/Gorisha2004/rag-news-chatbot-clean.git
cd rag-news-chatbot-clean
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
```
2. Setup API Key
bash
# Create .env file
echo "GOOGLE_API_KEY=your_new_key_here" > .env
Get key: ai.google.dev

3. Run Chatbot
bash
python main.py

📁 Project Structure
text
📁 rag-news-chatbot/
├── main.py                 # Entry point + chat loop
├── conversation_graph.py   # LangGraph agent logic
├── embedder.py            # Vector store + embeddings
├── data_fetcher.py        # RSS feeds
├── article_extractor.py   # News parsing
├── chunker.py            # Text splitting
├── retriever.py          # Semantic search
├── chat_history_manager.py # Conversation memory
├── .env                   # API keys (ignored)
├── .gitignore            # Secrets safe

🔧 Requirements
bash
pip install langchain langgraph langchain-community langchain-ollama langchain-huggingface
pip install sentence-transformers torch newspaper3k feedparser python-dotenv
pip install chromadb lxml_html_clean

👨‍💻 Author
Gorisha2004 - CS Student | RAG Systems | Placement Prep

