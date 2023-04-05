def fill_list_with_odd_numbers(func):
    split_func = func.split()
    odd_numbers_sheet = []
    count = 0
    dictionary_the_element_order = {}
    for i in split_func:
        if int(i) % 2 == 1:
            odd_numbers_sheet.append(i)
            count += 1
            dictionary_the_element_order[count] = i
    return dictionary_the_element_order


input_func = fill_list_with_odd_numbers(input('тут '))
print(input_func)
