class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # this method is always calling when we want to get some existing class attribute
    def __getattribute__(self, item):
        # Self - link to the instance of the class.
        # print('__getattr__')
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f"Setting attribute '{key}' value {value}")
        if value == 100:
            raise ValueError('Sorry, but value should not be 100')
        else:
            object.__setattr__(self, key, value)

    # this method is always calling when we want to get some NON-existing class attribute
    def __getattr__(self, item):
        return f"Item '{item}' does not exist"

    def __delattr__(self, item):
        print(f'Deleting attribute: {item}')
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
# a = pt1.x
# print(a)
# a = pt1.y
# print(a)
# pt1.x = 100
pt1.y = 200
# print(pt1.y)
print(pt1.qwe)
pt1.qwe = 101
print(pt1.qwe)
del pt1.qwe
print(pt1.__dict__)