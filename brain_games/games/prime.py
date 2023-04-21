from random import randint

TEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_OF_THE_RANGE = 2
END_OF_THE_RANGE = 100


def is_prime(number):
    counter = 0
    for n in range(1, int(number / 2)):
        if number % n == 0:
            counter += 1
    return counter <= 1


def question_answer_return():
    question = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
