import csv
from game_status import GameStatus


class Game:

    def __init__(self, path='', limit_of_errors=3):
        self.path = path
        self.limit_of_errors = limit_of_errors
        self.errors = 0
        self.__game_status = GameStatus.NOT_STARTED

        with open(path+'Questions.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            data = []
            for row in csv_reader:
                for item in row:
                    data.append(item.split(';'))

        self.__data = data
        self.data_index = 0

        if self.__data:
            self.__game_status = GameStatus.IN_PROGRESS

    def current_question(self):
        print(self.__data[self.data_index][0])

    def next_question(self):
        self.data_index += 1
        print(f"The next question is: '{self.__data[self.data_index][0]}'.")

    def give_an_answer(self, answer):
        if answer.lower() == self.__data[self.data_index][1].lower() and self.errors < self.limit_of_errors:
            print('You are right! ' + self.__data[self.data_index][2])
        else:
            print("You are wrong :(")
            self.errors += 1
            print(f"You can make {self.limit_of_errors-self.errors} mistakes.")

    @property
    def game_status(self):
        return self.__game_status

