from random import random
from typing import Iterable

from game_status import GameStatus


class Game:
    def __init__(self, allowed_misses: int = 6):
        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError('Number of allowed misses should be between 5 and 8')

        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ""

    def generate_word(self) -> str:
        filename = "WordsStockRus.txt"
        words = []
        with open(filename, encoding='utf-8') as file:
            for line in file:
                words.append(line.strip('\n'))

        rand_index = random.randint(0, len(words)-1)

        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.__word]

        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.__tries_counter


    @property
    def game_status(self):
        return self.__game_status

    @property
    def word(self):
        return self.__word

    @property
    def allowed_misses(self):
        return self.__allowed_misses

    @property
    def tries_counter(self):
        return self.__tries_counter

    