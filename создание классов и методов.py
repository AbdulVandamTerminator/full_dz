class Create_Anymals:
    def __init__(self, anymal='Существо призрак',
                 description='Существо только найдено и еще не изучено ни кем',
                 height='рост не известен',
                 weight='оно ничего не весит',):
        self.__height = height
        self.__weight = weight
        self.__anymal = anymal
        self.__description = description

    def name_anymal(self, name_an):
        '''
        :param name_an: Воод имени
        :return:
        '''
        self.__anymal = name_an
        return self.__anymal

    def set_description_anymal(self, description_set):
        '''
        :param description_set: ввод информации о существе
        :return:
        '''
        self.__description = description_set
        return self.__description

    def set_height(self, height, unit='см'):
        '''
        :param height: Размер существа
        :param unit: еденица измерения размера
        :return:
        '''
        self.__height = f'его рост {height} {unit.casefold()}'
        return self.__height

    def set_weight(self, weight, unit='кг'):
        '''
        :param weight: вес существа
        :param unit: еденица измерения веса
        :return:
        '''
        self.__weight = f'его вес {weight} {unit.casefold()}'

    def return_anymal(self):
        '''
        :return: возвращает созданное животное ввиде словаря
        '''
        animal_and_description = {}
        animal_and_description[self.__anymal.title()] = f'{self.__description.casefold()},' \
                                                        f' {self.__weight},' \
                                                        f' {self.__height}'
        return animal_and_description


my_dog = Create_Anymals()
my_dog.name_anymal('обезьяна')
my_dog.set_description_anymal('Он ест детей')
print(my_dog.return_anymal())

my_cat = Create_Anymals()
my_cat.set_height(123, 'м')
my_cat.set_weight(500, 'тонн')
print(my_cat.return_anymal())
