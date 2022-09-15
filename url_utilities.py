from os import strerror
from urllib import request
from urllib.error import URLError

def fetch_content(url):
  try: 
    response = request.urlopen(url)
    return response.read()
  except URLError:
    print("Error opening url: ", URLError)
  except IOError as e:
    print("I/O Error: ", strerror(e.errno))