from random import randint
from random import choice

RULE = 'What number is missing in the progression?'
RANGE_START = 2
INITIAL_ELEM_RANGE_END = 60
COMMON_DIFFERENCE_RANGE_END = 6
POSITIONS_IN_LINE = 11


def prog_line(initial_element, common_difference, positions_in_line):
    previous = initial_element
    line = []

    for n in range(positions_in_line):
        current = previous + common_difference
        previous = current
        line.append(current)
    return line


def question_string(line):
    random_number = choice(line)
    number_index = line.index(random_number)
    line[number_index] = '..'
    question = ' '.join(map(str, line))
    return question, random_number


def get_round():
    initial_element = randint(RANGE_START, INITIAL_ELEM_RANGE_END)
    common_difference = randint(RANGE_START, COMMON_DIFFERENCE_RANGE_END)
    question, random_number = question_string(
        prog_line(initial_element, common_difference, POSITIONS_IN_LINE))
    answer = str(random_number)
    return question, answer
