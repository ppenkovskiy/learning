# Class Point with protected attrs.
# class Point_1:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#
# pt = Point_1(1, 2)
# print(pt._x, pt._y)
# pt._x = 3
# pt._y = 4
# print(pt._x, pt._y)


# Class Point with private attrs.
class Point_2:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(self, x, y):
        if type(x) not in (int, float) and type(y) not in (int, float):
            raise ValueError('Coordinates should be numbers.')
        else:
            pass

    # setter
    def set_coord(self, x, y):
        self.__check_value(x, y)
        self.__x = x
        self.__y = y
        return (self.__x, self.__y)

    # getter
    def get_coord(self):
        return self.__x, self.__y


pt = Point_2(1, 2)
pt.set_coord(3, 4)
print(pt.get_coord())