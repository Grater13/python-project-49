from random import randint
from brain_games import engine

test = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer


def start():
    engine.game_engine(game_logic, test)
