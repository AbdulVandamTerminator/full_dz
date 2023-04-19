class Triangle():
    def __init__(self, side_one, side_two, side_three):
        self.__side_one = side_one
        self.__side_two = side_two
        self.__side_three = side_three

    def __str__(self):
        return f' 1 сторона - ({self.__side_one}),' \
               f' 2 сторона - ({self.__side_two}),' \
               f' 3 сторона - ({self.__side_three})'

    def __add__(self, other):
        side_triangle_one = self.__side_one + other.__side_one
        side_triangle_two = self.__side_two + other.__side_two
        side_triangle_three = self.__side_three + other.__side_three
        return Triangle(side_triangle_one, side_triangle_two, side_triangle_three)

    def __sub__(self, other):
        side_triangle_one = self.__side_one - other.__side_one
        side_triangle_two = self.__side_two - other.__side_two
        side_triangle_three = self.__side_three - other.__side_three
        return Triangle(side_triangle_one, side_triangle_two, side_triangle_three)


triangle = Triangle(1, 2, 3)
print(triangle)

triangle_two = Triangle(2, 3, 4)
print(triangle_two)

triangle_three = triangle + triangle_two
print(triangle_three)

triangle_four = triangle - triangle_two
print(triangle_four)
