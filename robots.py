from urllib import robotparser

rp = robotparser.RobotFileParser()

scraping_rules = {} 

def parse_robots(baseurl):
  """
  Check whether url can be scraped
  """
  def request_rate():
    rrate = rp.request_rate("*")
    if rrate:
      scraping_rules["request_rate"] = f"{rrate.requests} / {rrate.seconds} [requests/seconds]"
    else:
      scraping_rules["request_rate"] = None

  def crawl_delay():
    crawl_delay = rp.crawl_delay("*")
    if crawl_delay: 
      scraping_rules["crawl_delay"] = crawl_delay
    else: 
      scraping_rules["crawl_delay"] = None

  def can_scrape(baseurl):
    scraping_rules["can_fetch"] = rp.can_fetch("*", baseurl)

  rp.set_url(baseurl + "/robots.txt")
  rp.read()

  request_rate()
  crawl_delay()
  can_scrape(baseurl)

def can_fetch(baseurl):
  parse_robots(baseurl)
  return scraping_rules["can_fetch"]