class Cell:
    def __init__(self, mine, around_mines=0 ,fl_open= False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    pass


around_mines1 = 2
mine1 = True
c1 = Cell(around_mines1, mine1)
print(c1.around_mines)
print(c1.mine)
