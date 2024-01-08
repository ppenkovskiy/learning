import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and isinstance(filter, Mechanical):
            self.slot_1 = filter
        if slot_num == 2 and isinstance(filter, Aragon):
            self.slot_2 = filter
        if slot_num == 3 and isinstance(filter, Calcium):
            self.slot_3 = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def water_on(self):
        date_ok = []
        slots = [self.slot_1, self.slot_2, self.slot_3]

        if not all(slots):
            return False

        for s in slots:
            if 0 <= (time.time() - s.date) <= self.MAX_DATE_FILTER:
                date_ok.append(True)
            else:
                date_ok.append(False)

        return all(date_ok)


class Filter:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and hasattr(self, key):
            pass
        if key not in self.__dict__ and value > 0 and type(value) == float:
            object.__setattr__(key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
print(my_water.get_filters())
my_water.remove_filter(2)
print(my_water.get_filters())
