import requests
from bs4 import BeautifulSoup

url = 'http://www.jadwalsholat.pkpu.or.id/'
contents = requests.get(url)

soup = BeautifulSoup(contents.text, "html.parser")
data = soup.find_all('tr', class_='table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['shubuh'] = d.get_text()
    elif i == 2:
        sholat['dzuhur'] = d.get_text()
    elif i == 3:
        sholat['ashr'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1
print(sholat)
print(sholat['ashr'])

