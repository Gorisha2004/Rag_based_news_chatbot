import feedparser

rss_feeds = [
    "https://economictimes.indiatimes.com/rssfeedstopstories.cms", 
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms", 
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    #"https://news.google.com/rss/search?q=stock+market+india",
]

def fetch_articles_from_rss():
  articles = []
  for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)
    print(f"Fetching from Feed: {feed.feed.get('title', 'Unknown Feed')} - {feed_url}")
    for entry in feed.entries:
      article_data = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.get("published", "no date"),
        "summary": entry.get("summary", ""),
      }
      articles.append(article_data)
  return articles
