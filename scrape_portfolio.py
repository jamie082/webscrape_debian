# http://debian.org/doc/manuals/debian-handbook/

from bs4 import BeautifulSoup
import requests
import re

website = requests.get('http://debian.org/doc/manuals/debian-handbook/')
soup = BeautifulSoup(website.content, 'html.parser')

# dt, dd, dl HTML tags
links_find = soup.find(class_='book')
links_find_search = links_find.find_all('a')

for soup in links_find_search:
    names = links_find.contents[0]
    print (soup.string)

#  second additional code to extract link to either pandas or export to XML document

# find all the anchor tags with "href" 
# attribute strting with "http"

for link in soup.find_all('a', attrs={'attrs="href': re.compile("^http://")}):

    # display the actual urls

    print(link.get('href'))