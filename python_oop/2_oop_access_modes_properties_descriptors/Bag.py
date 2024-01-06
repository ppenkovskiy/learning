class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if thing.weight <= (self.max_weight - self.get_total_weight()):
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        total_weight = 0
        if self.__things:
            for thing in self.__things:
                total_weight += thing.weight
        return total_weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
print(bag.get_total_weight())
bag.add_thing(Thing("Котелок", 500))
print(bag.get_total_weight())
bag.add_thing(Thing("Спички", 20))
print(bag.get_total_weight())
bag.add_thing(Thing("Бумага", 100))
print(bag.get_total_weight())
bag.add_thing(Thing("Бумага_2", 300))
print(bag.get_total_weight())

