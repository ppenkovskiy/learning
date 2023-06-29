from game_result import GameResult
from game import Game, GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions asked: {result.questions_passed}. Mistakes made: {result.mistakes_made}.")
    print(f"You won!" if result.won else 'You lost')


game = Game('Questions.csv', 3, end_of_game_handler)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")
    print(q.text)
    answer = input() == 'y'

    if q.is_true == answer:
        print('Good job! You are right')
    else:
        print(f'You are mistaken. Here is the explanation: {q.explanation}')

    game.give_answer(answer)

