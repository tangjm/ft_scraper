import re
import datetime
from bs4 import BeautifulSoup

def extract_articles(source, mode):
  """
  Populate articles dictionary with mappings from titles to links
  """
  # <title> : <uri>
  articles_dict = {}
  
  soup = BeautifulSoup(source, 'html.parser')

  # Retrieve article <a> tags
  articles = soup.find_all(attrs={"data-trackable-context-story-link": re.compile("heading-link")})

  # Article links correspond to the "href" attribute within their <a> tags
  # Article titles are contained in the final <span> tag within the <a> tag
  for article in articles: 
    article_uri = article["href"] 
    article_title = article.contents[-1].string 
    article_title = re.sub(r'\n', '', article_title)
    article_title = article_title.split()
    article_title = " ".join(article_title)

    if article_title not in articles_dict:
      articles_dict[article_title] = article_uri

  total_articles = f"Total articles: {len(articles_dict)}"
  total_articles_len = len(total_articles)

  print("-"*total_articles_len)
  print(current_datetime())
  print(total_articles)
  print("-"*total_articles_len)

  if mode == "print":
    print_articles(articles_dict)
  elif mode == "save":
    save_articles(articles_dict)

def save_articles(articles_dict):
  """
  Save article titles to summary file with utf8 encoding
  """
  summary_file = open("summary.txt", "w", encoding="utf-8")
  for article in sorted(articles_dict.keys()):
    print(article, file=summary_file)
  summary_file.close()

def print_articles(articles_dict):
  """
  Print article titles to terminal
  """
  for article in sorted(articles_dict.keys()):
    print(article)

def current_datetime():
  yyyymmdd_hhmmss = r'(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}):(\d{2})'
  current_datetime = datetime.datetime.now()
  match = re.search(yyyymmdd_hhmmss, str(current_datetime))
  year = match.group(1)
  month = match.group(2)
  day = match.group(3)
  hours = match.group(4)
  minutes = match.group(5)
  seconds = match.group(6)
  current_datetime_formatted = f"Datetime: {day}/{month}/{year} {hours}:{minutes}:{seconds}"
  return current_datetime_formatted

