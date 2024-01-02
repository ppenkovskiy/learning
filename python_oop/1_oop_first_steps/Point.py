# class Point:
#     color = 'red'  # class attribute
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# # pt1 = Point()
# # pt2 = Point()
# # pt1.set_coords(1, 2)
# # pt2.set_coords(10, 20)
# # print(pt1.get_coords())
# # print(pt2.get_coords())
# # print(pt1.__dict__)


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Deleting instance: {str(self)}.')

    def get_coords(self):
        return self.x, self.y

pt = Point(1, 2)
print(pt.__dict__)
# Deleting 'pt' because there is no external references to this class instance.
