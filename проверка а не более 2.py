def number_of_characters(func):
    list_t = {}
    for i in func:
        if i not in list_t:
            list_t[i] = 1
        else:
            list_t[i] += 1
    return list_t


def checking_the_number_of_characters(save_func):
    sheet_to_delete = []
    sheet_to_save = []
    dictionary_tuple = ()
    dictionary_tuple = save_func.items()
    for i2 in dictionary_tuple:
        values_from_the_tuple = i2
        if values_from_the_tuple[1] == 2:
            sheet_to_delete.append(values_from_the_tuple)
            print(f'удалено --- {values_from_the_tuple[0]}')
        else:
            sheet_to_save.append(values_from_the_tuple[0])
    return f"сохранено {sheet_to_save}"


save_func = number_of_characters(input('Веди все что угодно '))
input_func = checking_the_number_of_characters(save_func)
print(input_func)
