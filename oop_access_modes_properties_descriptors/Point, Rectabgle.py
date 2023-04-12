class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        if type(a) == Point:
            self.a = a.get_coords()[0]
            self.b = a.get_coords()[1]
            self.c = b.get_coords()[0]
            self.d = b.get_coords()[1]
            self.__sp = Point(self.a, self.b)
            self.__ep = Point(self.c, self.d)
        else:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.__sp = Point(self.a, self.b)
            self.__ep = Point(self.c, self.d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: ({self.a}, {self.b}) ({self.c}, {self.d})')

