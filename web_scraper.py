import requests
from bs4 import BeautifulSoup

r = requests.get('https://se.com')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)

print(soup.meta)

print(soup.title.parent.name)
