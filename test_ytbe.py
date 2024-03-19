#BeautifulSoup vs requests

#1. BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

html_page = urlopen("https://keebs.gg/builds#sort=recent&page=1")
soup = BeautifulSoup(html_page, "html.parser")

for link in soup.find_all('a'):
    if "/builds/" in str(link):
        print("https://keebs.gg" + link.get('href'))
        
        
#2. requests

from lxml import html
import requests

page = requests.get('https://keebs.gg/builds#sort=recent&page=1')
webpage = html.fromstring(page.content)

items = webpage.xpath('//a/@href')

for item in items:
    if "/builds/" in str(item):
        print("https://keebs.gg" + str(item))