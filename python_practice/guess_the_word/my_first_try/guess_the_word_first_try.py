import random


class GuessTheWord:

    def __init__(self, mistakes=10):
        with open('../WordsStockRus.txt', mode='r', encoding='utf-8') as file:
            words = file.readlines()
            word = words[random.randint(0, len(words) - 1)].strip()
        self.mistakes = mistakes
        self.__word = list(word)
        self.word = list(len(self.__word) * '*')
        self.guessed_letters = []

    def print_the_word(self):
        print(''.join(self.word))

    def guess_the_letter(self, letter):
        self.guessed_letters.append(letter)
        flag = True
        for i in range(len(self.word)):
            if letter == self.__word[i]:
                self.word[i] = self.__word[i]
                print(f'You guessed the letter "{letter}"')
                flag = False
        if flag:
            self.mistakes -= 1
            print(f'Rights to the mistake: {self.mistakes}')


w = GuessTheWord()
print(f"Your word: {''.join(w.word)}")

while w.mistakes >= 1:
    print("Guess the letter: ")
    w.guess_the_letter(input())
    print(''.join(w.word))

if '*' not in w.word:
    print('You win')
else:
    print('You lose')
