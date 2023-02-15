# http://debian.org/doc/manuals/debian-handbook/

from bs4 import BeautifulSoup
import requests
import re

# https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

website = requests.get('http://debian.org/doc/manuals/debian-handbook/')
soup = BeautifulSoup(website.text, 'html.parser')

# dt, dd, dl HTML tags

two_find_list = soup.find(class_='book')
two_find_list_items = two_find_list.find_all('a')

for list_name in two_find_list_items:
    names = list_name.contents[0]
    print(names)


#  second additional code to extract link to either pandas or export to XML document

# find all the anchor tags with "href" 
# attribute strting with "http"
