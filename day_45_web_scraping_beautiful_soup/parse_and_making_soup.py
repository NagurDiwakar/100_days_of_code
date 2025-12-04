from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup)

# to get all the anchor tags

anchor_tags = soup.find_all(name='a')
print(anchor_tags)