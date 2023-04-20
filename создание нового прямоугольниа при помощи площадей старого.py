class Rectangle():
    def __init__(self, side_one, side_two):
        self.__side_one = side_one
        self.__side_two = side_two
        self.rectangle_area = self.__side_one * self.__side_two

    def __str__(self):
        width = self.__side_one / 2 + 2
        height = self.__side_one / 2 - 2
        if height < 1:
            height = 1
        if width < 1:
            width = 2
        return f'Ширина - {width}, высота - {height},\n'\
               f'минимальная ширина = 2, минимальная высота = 1'

    def __add__(self, other):
        rectangle = self.rectangle_area + other.rectangle_area
        return Rectangle(rectangle, 1)

rectangle_one = Rectangle(1, 1)

rectangle_two = Rectangle(1, 1)

rectangle_three = rectangle_one + rectangle_two
print(rectangle_three)
