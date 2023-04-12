from random import randint
from math import gcd

test = 'Find the greatest common divisor of given numbers.'


def game_logic():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = str(number1) + ' ' + str(number2)
    answer = gcd(number1, number2)
    return question, answer
