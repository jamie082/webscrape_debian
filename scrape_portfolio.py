# http://debian.org/doc/manuals/debian-handbook/

from bs4 import BeautifulSoup
import requests

website = requests.get('http://debian.org/doc/manuals/debian-handbook/')
soup = BeautifulSoup(website.content, 'html.parser')

# dt, dd, dl HTML tags
links_find = soup.find(class_='book')
links_find_search = links_find.find_all('a')

for soup in links_find_search:
    names = links_find.contents[0]
    print(soup.string)

#  second additional code to extract link to either pandas or export to XML document

images_list = []

images = soup.select('a')
for xml_document in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for image in images_list:
    print(image)