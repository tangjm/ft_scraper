from urllib import request

def fetch_content(url):
  try: 
    response = request.urlopen(url)
    return response.read()
  except:
    print("Request failed")
