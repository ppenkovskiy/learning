class Tutorial:
    title = 'Class attribute' # class attribute

    def __init__(self, name):
        self.name = name  # local attribute (local property)


t = Tutorial('Lesson_0')
print(t.__dict__)  # output of local properties of a class object
print(Tutorial.__dict__)  # output of class attributes
