from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_articles(full_articles):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    add_start_index = True
  )

  documents = []
  for article in full_articles:
    doc = Document(
      page_content = article["content"],
      metadata = {
        "title": article['title'],
        "link": article['link'],
        "published": article["published"],
      }
    )
    chunks = text_splitter.split_documents([doc])
    documents.extend(chunks)
  print(f"Split {len(full_articles)} articles into {len(documents)} chunks.")
  return documents