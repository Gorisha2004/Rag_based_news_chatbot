import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(documents):
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it properly.")
    
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        # 100% FREE, offline, fast!
    )
    vector_store = InMemoryVectorStore(embeddings)

    document_ids = vector_store.add_documents(documents)
    print(f"Added {len(document_ids)} document chunks to vector store.")
    return vector_store
