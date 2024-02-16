import requests
from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

r = requests.get('https://www.cbr-xml-daily.ru/archive/2024/02/14/daily_json.js')
# r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
for valute, data in r.json()['Valute'].items():
    print(valute, str(today), data['Value'])