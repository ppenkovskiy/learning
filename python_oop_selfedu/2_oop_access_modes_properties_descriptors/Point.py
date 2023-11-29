class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt.x)
pt.x = 3
print(pt.x)