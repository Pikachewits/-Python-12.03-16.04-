import requests
import xml.etree.ElementTree as ET
import decimal
import datetime


def currency_rates(val_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    root = ET.fromstring(response)

    for item in root.findall('Valute'):
        char_code = item.find('CharCode').text

        if char_code == val_code.upper():
            value = decimal.Decimal(item.find('Value').text.replace(',', '.'))
            data_list = [int(element) for element in root.attrib['Date'].split('.')[::-1]]
            data = datetime.date(*data_list)
            print(f'[{data}] {val_code} = {value} руб.')

currency_rates('usd')
