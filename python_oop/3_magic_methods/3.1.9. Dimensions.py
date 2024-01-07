class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__a = value
        else:
            return

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__b = value
        else:
            return

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__c = value
        else:
            return

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super(Dimensions, self).__setattr__(key, value)
