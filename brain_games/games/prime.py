from random import randint

TEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    question = randint(2, 100)
    counter = 0

    for n in range(1, int(question / 2)):
        if question % n == 0:
            counter += 1
        answer = 'yes' if counter <= 1 else 'no'
    return question, answer
