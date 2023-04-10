from collections import Counter



def making_friends_and_items():
    dictionary_of_names_and_things = {}
    storage_of_things = []
    count = 0
    whiile_stop = ''
    while whiile_stop != '1':
        name = input('Имя вашего друга: ')
        item = input(f'вещь вашего друга {name}: ')
        storage_of_things.append(set(item.split()))
        things_separately = item.split()
        count += 1
        dictionary_of_names_and_things[name + str(count)] = things_separately
        whiile_stop = input('Конец ? ')
    return dictionary_of_names_and_things, storage_of_things
#Создание друзей и деление их и их вещей по категориям списков для разных нужд<<<--------------


making_friends_and_items, storage_of_things = making_friends_and_items()


def the_same_things(func):
    list_all_elements_without_repetitions = []
    list_repetitive_things = []
    for i in func:
        for i2 in i:
            list_all_elements_without_repetitions.append(i2)
            unting_elements = Counter(list_all_elements_without_repetitions)
    for key, value in unting_elements.items():
        if value > 1:
            list_repetitive_things.append(key)
    return list_repetitive_things
#Элементы которые есть у вех друзей <<<---------------------------------------------------------


the_same_things = the_same_things(storage_of_things)


def deleting_identical_items(deliter, storage_of_things):
    full_list_things = []
    list_name = []
    for key, value in deliter.items():
        try:
            get_rid_of_sameness = set(value)
            for i in storage_of_things:
                get_rid_of_sameness.remove(str(i))
            print(f'Список уникальных вещей {key}: {get_rid_of_sameness}')
        except KeyError:
            pass
        except ValueError:
            pass
    print('------------------------------------------------------------------')
    print(f'Cписок не уникальных вещей: {storage_of_things}')
    print('------------------------------------------------------------------')
    for key1, value2 in deliter.items():
        for i in value2:
            full_list_things.append(i)
    print(f'Это полный список их вещей: {full_list_things}')
    return storage_of_things
#Удаление из списков друзей элементы которые есть у всех и полный вывод статистики <<<-------------


deleting_identical_items = deleting_identical_items(making_friends_and_items, the_same_things)


#третий пункт я не сделал
