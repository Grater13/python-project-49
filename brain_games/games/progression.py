from random import randint

test = 'What number is missing in the progression?'


def game_logic():
    first_num = randint(2, 60)
    prog = randint(2, 5)
    prev = first_num
    list = []

    for n in range(11):
        current = prev + prog
        prev = current
        list.append(current)

    random_position = randint(0, 9)
    answer = list[random_position]
    list[random_position] = '..'
    question = ' '.join(map(str, list))
    return question, answer
