def retrieve_similar_documents(vector_store, query, k = 3):
  """
    Given a user query, returns top-k most relevant news chunks from the vector store.
  """
  results = vector_store.similarity_search(query, k=k)
  return results