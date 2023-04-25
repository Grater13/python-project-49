from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_START = 2
RANGE_END = 100


def is_prime(number):
    for n in range(2, number):
        if number % n != 0:
            continue
        else:
            return False
    return True


def question_answer_return():
    question = randint(RANGE_START, RANGE_END)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
