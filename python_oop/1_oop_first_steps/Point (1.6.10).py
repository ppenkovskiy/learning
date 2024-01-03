from copy import deepcopy


class Point:
    obj = None

    def __new__(cls, *args, **kwargs):
        cls.obj = super().__new__(cls)  # creating new object of class DB
        return cls.obj

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj_2 = deepcopy(self.obj)
        return obj_2


pt = Point(1, 2)
pt_deep_clone = pt.clone()
print(id(pt))
print(id(pt_deep_clone))
