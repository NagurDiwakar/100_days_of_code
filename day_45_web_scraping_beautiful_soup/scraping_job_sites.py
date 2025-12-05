from bs4 import BeautifulSoup

import requests

#webpage = requests.get("https://example.com")
webpage = requests.get("https://news.ycombinator.com/")
webpage_text = webpage.text
#print(webpage_text)

articles = BeautifulSoup(webpage_text, "html.parser")
article_titles = articles.find_all(name="span", class_="titleline")

for article_tag in article_titles:
    article_text = article_tag.getText()
    article_link = article_tag.find("a").get("href")
    print(f"Title: {article_text}")
    print(f"Link: {article_link}\n")
