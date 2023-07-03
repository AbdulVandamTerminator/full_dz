from bs4 import BeautifulSoup
import requests
from pprint import pprint



list_input = []
list_output_res = []
slov = {}


def Pars_Slov():
    URL = 'https://www.anekdot.ru/'

    get_rec = requests.get(URL)
    html = BeautifulSoup(get_rec.text, 'lxml')

    result = html.find_all("div", class_="text")
    for i in result:
        list_input.append(i.text)
    list_output_res.append(list_input)
    return list_output_res


def sort_def(atrg):
    count = 0
    for i2 in list_output_res:
        for i3 in i2:
            count += 1
            slov[count] = i3
    return slov, count

sort_on = sort_def(Pars_Slov())




# def User_Sort(sort, input_args):
#     if input_args <= sort[1] and input_args != 0:
#         return sort[0][input_args]
#     else:
#         return 'Такого значения нет'
#
#
# User_Sort_on = User_Sort(sort_on, 2)


