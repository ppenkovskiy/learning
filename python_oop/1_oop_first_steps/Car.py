class Car:
    pass


setattr(Car, 'model', "Toyota")
setattr(Car, 'color', "Pink")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])
