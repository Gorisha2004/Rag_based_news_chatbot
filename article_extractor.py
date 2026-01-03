from newspaper import Article

def fetch_full_article_content(url):
  try:
    article = Article(url)
    article.download()
    article.parse()
    return article.text
  except Exception as e:
    print(f"Failed to extract article from {url}: {e}")
    return ""
  
def extract_full_articles(rss_articles):
  full_articles = []
  for art in rss_articles:
    content = fetch_full_article_content(art["link"])
    if content:
      full_articles.append({
        "title": art["title"],
        "link": art["link"],
        "published": art["published"],
        "content": content,
        })
  return full_articles