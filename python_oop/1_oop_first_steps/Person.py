class Person:
    name = 'Name'
    job = 'Engineer'
    city = 'City'


p1 = Person()

print('job' in p1.__dict__)
