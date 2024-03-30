import os

import requests

from bs4 import BeautifulSoup
import urllib.request

URL = "https://ru.wallpaper.mob.org/gallery/tag=priroda/"
response = requests.get(URL)
print(response)

bs = BeautifulSoup(response.text, 'lxml')

temp = bs.find('div', 'tag-mini-widget__title-wrap')
print(temp)
print(temp.text.strip())

titles = bs.find_all('div', 'tag-mini-widget__title-wrap')

for title in titles:
    print(title.text.strip())

images = bs.find_all('img', 'image-gallery-image__image')

image_links = []
for image in images:
    image_links.append(image.get("src"))

print(image_links)