import copy


class Graph:
    def __init__(self, data, is_show=True):
        self.data = copy.copy(data)
        self.is_show = is_show

    def set_data(self, data):
        self.data = copy.copy(data)

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print('Графическое отображение данных:', *self.data)
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print('Столбчатая диаграмма:', *self.data)
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show):
        self.is_show = fl_show



data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()