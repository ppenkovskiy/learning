from game import Game
from game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f"Remaining tries = {game.remaining_tries}.")

print(f"The word consists of {letters_count} letters.")
print('Try to guess the letter: ')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick a letter. \n")
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f"Remaining tries = {game.remaining_tries}.")
    print(f"Tried letters = {chars_list_to_str(game.tried_letters)}")

if game.game_status == GameStatus.LOST:
    print('You are hanged')
    print(f'The word was: {game.word}')
else:
    print('Congratulations, you won!')
