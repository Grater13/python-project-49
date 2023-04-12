from random import randint
from math import gcd
from brain_games import engine

test = 'Find the greatest common divisor of given numbers.'


def game_logic():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = str(number1) + ' ' + str(number2)
    answer = gcd(number1, number2)
    return question, answer


def start():
    engine.game_engine(game_logic, test)
