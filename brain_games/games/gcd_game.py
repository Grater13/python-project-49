from random import randint
from math import gcd

TEST = 'Find the greatest common divisor of given numbers.'
START_OF_THE_RANGE = 1
END_OF_THE_RANGE = 10


def question_answer_return():
    number1 = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    number2 = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    question = str(number1) + ' ' + str(number2)
    answer = gcd(number1, number2)
    return question, str(answer)
