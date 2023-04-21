from random import randint

TEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_START = 2
RANGE_END = 100


def is_prime(number):
    counter = 0
    for n in range(1, number):
        if number % n == 0:
            counter += 1
    return counter <= 1


def question_answer_return():
    question = randint(RANGE_START, RANGE_END)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
