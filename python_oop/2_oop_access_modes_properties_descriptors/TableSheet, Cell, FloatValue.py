class FloatValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, N, M):
        self.cells = []
        iterator = 1.0
        for i in range(N):
            self.cells.append([])
            for j in range(M):
                self.cells[-1].append(Cell(iterator))
                iterator += 1

th = TableSheet(5,3)