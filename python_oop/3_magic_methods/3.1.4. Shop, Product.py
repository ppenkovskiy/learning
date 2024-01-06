class Product:
    iterator = 1

    @classmethod
    def iterator_plus_one(cls):
        cls.iterator += 1

    def __init__(self, name, weight, price):
        self.id = self.iterator
        self.name = name
        self.weight = weight
        self.price = price

        self.iterator_plus_one()

    def __setattr__(self, key, value):
        if key == 'id' and type(value) == int and value >= 1:
            object.__setattr__(self, key, value)
        elif key in ('weight', 'price') and type(value) in (int, float) and value >= 0:
            object.__setattr__(self, key, value)
        elif key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")