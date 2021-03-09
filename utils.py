import requests
from decimal import Decimal
import datetime


def currency_rates(name_currency):
    currency = name_currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    now_day = int(content[content.find('<ValCurs Date="') + 15:content.find('<ValCurs Date="') + 17])
    now_month = int(content[content.find('<ValCurs Date="') + 18:content.find('<ValCurs Date="') + 20])
    now_year = int(content[content.find('<ValCurs Date="') + 21:content.find('<ValCurs Date="') + 25])
    now_date = datetime.datetime(day=now_day, month=now_month, year=now_year)
    print(f'Курс {name_currency.upper()} на текущую дату: {now_date.date()}')
    if content.find(currency) != -1:
        currency = (content[content.find(currency):])
        currency = currency[currency.find('<Value>') + 7:currency.find('</Value>')]
        currency = Decimal(currency.replace(',', '.'))
    else:
        currency = "None"
    return currency
