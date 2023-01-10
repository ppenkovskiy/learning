class Person:
    name = 'Pavel Penkovskiy'
    job = 'Programmer'
    city = 'Minsk'


p1 = Person()

print('job' in p1.__dict__)