class Basic_Properties():
    def __init__(self, model):
        self.__model = model
        self._year = None
        self._color = None
        self._price = None
        self._power = None
        self._start = False
        print(f'\nКласс {self.__class__.__name__}')

    def start_transport(self):
        self._start = True
        return f'Транспорт заведен'

    def properties(self, year, color, power, price):
        self._year = year
        self._color = color
        self._price = price
        self._power = power
        return f'Год: {year}, цвет: {color}, мощность: {power}, цена: {price}'

    def __str__(self):
        return f' Год: {self._year}\n' \
            f' цвет: {self._color}\n' \
            f' мощность: {self._price}\n' \
            f' цена: {self._power}\n' \
            f' модель: {self.__model}'




class Car(Basic_Properties):
    def __init__(self, model):
        super().__init__(model)
        self.__model = model
    def mileage(self, number):
        self.__number = number

    def journey(self, where_from, where):
        self.__where = where
        self.__where_form = where_from

    def __str__(self):
        if self._start == True:
            return f'{super().__str__()}\n' \
                f' пробег авто: {self.__number}\n' \
                f' машина заведена и готова к отправке.\n'\
                f' Ваша {self.__model} отправляется из {self.__where_form}, в {self.__where}'
        else:
            return f'{super().__str__()}\n' \
                f' пробег авто: {self.__number}\n' \
                f' машина не заведена'



class Plane(Basic_Properties):
    def __init__(self, model):
        super().__init__(model)
        self.__purpose = 'Летад летал, взрывал что то'
        self.__country = 'Сам както появился'
    def purpose(self, purpose):
        self.__purpose = purpose
        return self.__purpose

    def country_of_creation(self, country):
        self.__country = country
        return self.__country

    def __str__(self):
        return f'{super().__str__()}\n' \
            f' Назночение: {self.__purpose}\n' \
            f' Страна создания: {self.__country}'

car2 = Car('Мазда')
car2.start_transport()
car2.properties(1989, 'красный', 450000, 100)
car2.mileage(250)
car2.journey('Россия', 'Луна')
print(car2)


plane = Plane('ПЕ-8')
plane.properties(1939, 'серый', 'Дорого', 250)
plane.purpose('бомбондировщик')
print(plane)
