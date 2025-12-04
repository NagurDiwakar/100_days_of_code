from bs4 import BeautifulSoup

import requests

webpage = requests.get("https://example.com")
webpage_text = webpage.text
print(webpage_text)

