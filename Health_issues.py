import requests

from bs4 import BeautifulSoup

"""hyperskill.org problem of the day"""
"""Script for scraping topic titles from 'https://www.who.int/health-topics' which starts from LETTER """

URL = 'https://www.who.int/health-topics'  # URL from which parsing topics titles
LETTER = 'S'  # letter with which topic name starts

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
soup = soup.find_all('a')
topics = []

for link in soup:
    if 'topics' in str(link) or 'entity' in str(link):  # some topics urls written as www.who.org/___ some just /topic/
        link_text = link.get_text('href')               # so we look for both types
        if len(link_text) > 1 and link_text[0] == LETTER:
            topics.append(link_text)

print(topics)
