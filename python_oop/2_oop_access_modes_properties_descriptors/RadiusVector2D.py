class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __check_value(self, x):
        return type(x) in (float, int) and self.MIN_COORD <= x <= self.MAX_COORD

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0

        if self.__check_value(y):
            self.__y = y

        if self.__check_value(x):
            self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_value(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_value(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


a = RadiusVector2D(1, 2)
print(a.x)
print(a.y)
a.x = 100
print(a.x)
a.y = 200
print(a.y)