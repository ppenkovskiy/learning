class Tutorial:
    title = 'class attribute'

    def __init__(self, name):
        self.name = name  # local attribute


t = Tutorial('lesson_0')
print(t.__dict__)  # output of local properties of a class object
print(Tutorial.__dict__)  # output of class attributes
