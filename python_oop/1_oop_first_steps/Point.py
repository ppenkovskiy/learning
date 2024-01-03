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
# The Python garbage collector removes 'pt' after program execution
# because there are no external references to this instance of the class
