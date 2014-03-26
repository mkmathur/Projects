'''
Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list.
'''

import requests
from bs4 import BeautifulSoup

def print_list(a):
	print "\n".join(a)
	print "\n=============\n"

url = raw_input('Enter URL: ')
choice = input("What to scrape?\n1. Links\n2. Images\n")
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content)

if choice == 1:
	urls = [link['href'] for link in soup.select('a[href^="http://"]')]
	print "URLs: \n"
	print_list(urls)
else:
	images = [image['src'] for image in soup.find_all("img")]
	print "Images: \n"
	print_list(images)
