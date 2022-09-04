import sys
import re
from bs4 import BeautifulSoup

filename = sys.argv[1]

# <title> : <href>
articles_dict = {}
base_url = "www.ft.com"

def extract_articles(filename):
  """
  Populate articles dictionary with mappings from titles to links
  """
  f = open(filename, 'rb')
  soup = BeautifulSoup(f, 'html.parser')
  f.close()

  # Retrieve article <a> tags
  articles = soup.find_all(attrs={"data-trackable-context-story-link": re.compile("heading-link")})

  # Article links correspond to the "href" attribute within their <a> tags
  # Article titles are the final <span> tag within the <a> tag
  for article in articles: 
    article_uri = article["href"] 
    article_title = article.contents[-1].string 
    article_title = re.sub(r'\n', '', article_title)
    article_title = article_title.split()
    article_title = " ".join(article_title)

    articles_dict[article_title] = article_uri

  print(f"Total articles: {len(articles_dict)}")

def save_articles():
  summary_file = open("summary.txt", "w", encoding="utf-8")
  for article in articles_dict:
    print(article, file=summary_file)
  summary_file.close()

def print_articles():
  for article in articles_dict:
    print(article)

def main():
  print(filename)
  extract_articles(filename)
  save_articles()
  print_articles()
  print(len(articles_dict))


if __name__ == '__main__':
  main()

