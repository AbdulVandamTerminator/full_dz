input_user = input('Посимволовая проверка - 0 на клавиатуре\n'
                   'Проверка слов - 1 на клавиатуре\n'
                   '-------------- ')

"""выбор как работать с введенными символами"""


def divisor_terms_and_symbols(input_func):
    dictionary_with_data_types = {'строка': None,
                                  'число': None,
                                  'список': None,
                                  'кортеж': None,
                                  'Булевое значение': None}
    list_string = []
    list_int = []
    list_lists = []
    list_tuple = []
    list_bool = []

    for i in input_func:
        if i.isdigit():
            list_int.append(int(i))
        elif i[0] == '[' and i[-1] == ']':
            list_lists.append(i)
        elif i[0] == '(' and i[-1] == ')':
            list_tuple.append(i)
        elif i == 'True' or i == 'False':
            list_bool.append(i)
        else:
            list_string.append(str(i))

    dictionary_with_data_types['строка'] = list_string
    dictionary_with_data_types['число'] = list_int
    dictionary_with_data_types['список'] = list_lists
    dictionary_with_data_types['кортеж'] = list_tuple
    dictionary_with_data_types['Булевое значение'] = list_bool
    list_tuple = [i for i in dictionary_with_data_types.items()]

    print(list_tuple[0])
    print(list_tuple[1])
    print(list_tuple[2])
    print(list_tuple[3])
    print(list_tuple[4])

    return dictionary_with_data_types
function_of_word_types = divisor_terms_and_symbols

"""функция с самодельной проверкой типов данных которые
   позже будут разложены по спискам и добавлены в кортеж"""


if input_user == '0':
    character_by_character_solution = input('Посимвольная проверка ("a", "1"...) --- ')
    print('-------------------------------------')
    function_of_word_types(character_by_character_solution)
elif input_user == '1':
    character_by_character_solution = input('Проверка слов ("Боб1", "1232si"...) --- ')
    print('-------------------------------------')
    function_of_word_types(character_by_character_solution.split())

"""проверка выбора пользователя"""

