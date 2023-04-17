from random import randint

TEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), answer
