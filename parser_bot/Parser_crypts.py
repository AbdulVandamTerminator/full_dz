from bs4 import BeautifulSoup
import requests



URL = "https://ru.investing.com/crypto/"
html = requests.get(URL)
bs = BeautifulSoup(html.text, "html.parser")

result_name = bs.find_all("td", class_="left bold elp name cryptoName first js-currency-name")
result_coins = bs.find_all("td", class_="price js-currency-price")


def output_name_coins():
    list_name = []
    list_coins = []
    list_name_coins = []
    count = -1
    for nm in result_name:
        list_name.append(nm.text.strip())
    for ci in result_coins:
        list_coins.append(ci.text.strip())
    return list_name, list_coins

