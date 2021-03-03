import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler/news')


soup = BeautifulSoup(html_doc.text, "html.parser")
populer = soup.find('div', class_='grid-row list-content')

titles = populer.find_all(class_='media__link')
images = populer.find_all(class_='media__image')

for image in images:
    print(image.find('a').find('img')['title'])