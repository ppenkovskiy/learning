# Class Point with private attrs.
class Point:

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)

    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Invalid coordinates")

    # setter (interface methods)
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
            return (self.__x, self.__y)
        else:
            raise ValueError("Invalid coordinates")

    # getter (interface methods)
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(3, 4)
print(pt.get_coord())