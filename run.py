import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler/news')

    soup = BeautifulSoup(html_doc.text, "html.parser")
    populer = soup.find('div', class_='grid-row list-content')

    titles = populer.find_all(class_='media__link')
    images = populer.find_all(class_='media__image')

    return render_template('detik-scrapper.html', images=images)

@app.route('/idr-exchange-rate')
def idr_exchange_rate():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-exchange-rate.html', datas=json_data.values())

if __name__ == '__main__':
    app.run(debug=True)