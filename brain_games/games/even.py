from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_OF_THE_RANGE = 1
END_OF_THE_RANGE = 100


def is_even(number):
    return number % 2 == 0


def question_answer_return():
    question = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    answer = 'yes' if is_even(question) else 'no'
    return str(question), answer
