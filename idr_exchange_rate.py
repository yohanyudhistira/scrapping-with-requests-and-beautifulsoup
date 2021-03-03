import requests


# json_data =requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 7.0012023723221e-05, 'date': 'Tue, 2 Mar 2021 12:00:01 GMT', 'inverseRate': 14283.260886063}, 'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.8183513114583e-05, 'date': 'Tue, 2 Mar 2021 12:00:01 GMT', 'inverseRate': 17186.999314233}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])