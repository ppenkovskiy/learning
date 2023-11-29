class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    # Setting "old" an object of the class property
    old = property(get_old, set_old)


p = Person('Person_1', 20)
print(p.old)
p.old = 35
print(p.old, p.__dict__)
