import os
from dotenv import load_dotenv
from data_fetcher import fetch_articles_from_rss
from article_extractor import extract_full_articles
from chunker import chunk_articles
from embedder import create_vector_store
from chat_history_manager import get_chat_history
from conversation_graph import create_conversation_graph
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
  session_id = "default_session"
  chat_history = get_chat_history(session_id)

  print("Step 1: Fetching articles metadata from rss feeds...")
  rss_articles = fetch_articles_from_rss()

  print("Step 2: Extracting full article content from URLs...")
  full_articles = extract_full_articles(rss_articles)

  print("Step 3: Chunking full articles for RAG indexing...")
  chunks = chunk_articles(full_articles)
  print(f"Total chunks: {len(chunks)}")

  chunks = chunks[:10]

  print("Step 4: Creating vector store with embeddings...")
  vector_store = create_vector_store(chunks)

  print("Setup complete. Vector store ready with embedded documents.")

  llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
  # llm = OllamaLLM(model="llama3.2")

  graph = create_conversation_graph(llm, vector_store)

  print("\nCharbot ready! Type 'exit' to quit.")

  while True:
    user_input = input("You: ")
    if user_input.strip().lower() == 'exit':
      break

    chat_history.add_user_message(user_input)

    state = {"messages": list(chat_history.messages[-10:])}

    outputs = None
    for output in graph.stream(state, stream_mode="values", config={"configurable": {"session_id": session_id}}):
      outputs = output

    bot_response = outputs["messages"][-1].content
    print(f"Bot: {bot_response}")

    chat_history.add_ai_message(bot_response)

if __name__ == "__main__":
  main()    

