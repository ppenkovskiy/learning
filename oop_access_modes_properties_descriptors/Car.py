class Car:
    def __init__(self, model=''):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 2 <= len(model) <= 100:
            self.__model = model

    @model.deleter
    def model(self):
        del self.__model


car = Car()
car.model = "Toyota"