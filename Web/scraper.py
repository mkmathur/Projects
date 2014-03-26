'''
Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list.
'''

import requests
from bs4 import BeautifulSoup

u = raw_input('Enter URL: ')
r = requests.get(u)
c = r.content
soup = BeautifulSoup(c)
links = soup.find_all("a")
print(links)
