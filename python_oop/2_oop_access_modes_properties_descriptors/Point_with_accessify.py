from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Invalid coordinates")

    @private
    @classmethod
    def check_value(cls, value):
        return type(value) in (int, float)

    # Setter (interface methods)
    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
            return (self.__x, self.__y)
        else:
            raise ValueError("Coordinates should be in (int, float)")

    # Getter (interface methods)
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(3, 4)
pt.check_value(5)
