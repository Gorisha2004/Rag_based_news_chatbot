import os
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_answer(retrieved_docs, user_query):
    """
    Given retrieved docs and user query, generates a concise news answer using Gemini.
    """
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    
    # llm = OllamaLLM(model="llama3.2")
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

    context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = (
        "You are a financial news assistant. "
        "Given the following context extracted from news articles and the user question, "
        "provide a clear, concise, and factual answer. "
        "If the answer is not in the context, say 'Sorry, no information available.'\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {user_query}\n"
        "Answer:"
    )

    answer = llm.invoke([{"role": "user", "content": prompt}])
    return answer.content