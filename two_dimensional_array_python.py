class Cell:
    def __init__(self, mine=False, around_mines=0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
