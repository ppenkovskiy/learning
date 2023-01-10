# https://stepik.org/lesson/701973/step/6?unit=702074


class Car:
    pass


setattr(Car, 'model', "Toyota")
setattr(Car, 'color', "Pink")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])
