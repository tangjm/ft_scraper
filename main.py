import sys
import url_utilities
import robots
from article_scraper import extract_articles

url = "https://www.ft.com"

def main():
  args = sys.argv[1:]

  # python main.py [--test] [--save-articles] [files ...]
  # python main.py --test --save-articles [files ...]
  # python main.py --test [files ...]
  # python main.py --save-articles
  # python main.py 
  test_run = False 
  if args and args[0] == "--test":
    test_run = True
    del args[0]

  mode = "print" 
  if args and args[0] == "--save-articles":
    mode = "save_articles"
    del args[0]

  if test_run:
    sample_files = args 
    print(sample_files)
    for file in sample_files:
      print("\n")
      print(f"Filename: {file}")
      f = open(file, "rb")
      extract_articles(f, mode)
      f.close()
  else:
    if not robots.can_fetch(url):
      print(f"Scraping is not permitted at {url}")
      sys.exit(1)
    html_content = url_utilities.fetch_content(url)
    extract_articles(html_content, mode)

if __name__ == '__main__':
  main()