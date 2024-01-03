class Point:
    def __new__(cls, *args, **kwargs):
        # cls - refers to the current CLASS
        print('Calling __new__ for ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        # self - refers to the created INSTANCE of the class
        print('Calling __init__ for ' + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)