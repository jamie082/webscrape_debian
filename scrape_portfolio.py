# http://debian.org/doc/manuals/debian-handbook/

from bs4 import BeautifulSoup
import requests
import csv
import re

# https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

website = requests.get('http://debian.org/doc/manuals/debian-handbook/')
soup = BeautifulSoup(website.text, 'html.parser')

# dt, dd, dl HTML tags

# Create a file to write to, add headers row
f = csv.writer(open('output.csv', 'w'))
f.writerow(['Name', 'Link'])

two_find_list = soup.find(class_='toc')
two_find_list_items = two_find_list.find_all('a')

for list_name in two_find_list_items:
    names = list_name.contents[0]
    links = 'URL' + list_name.get('href')


    # Add each artist's name and associated link to a row
    f.writerow([names, links])