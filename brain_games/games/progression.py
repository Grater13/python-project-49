from random import randint
from random import choice

RULE = 'What number is missing in the progression?'
RANGE_START = 2
INITIAL_ELEM_RANGE_END = 60
COMMON_DIFFERENCE_RANGE_END = 6


def prog_line(initial_element, common_difference):
    POSITIONS_IN_LINE = 11
    previous = initial_element
    line = []

    for n in range(POSITIONS_IN_LINE):
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


def question_answer_return():
    question, random_number = question_string(
        prog_line(
            randint(RANGE_START, INITIAL_ELEM_RANGE_END),
            randint(RANGE_START, COMMON_DIFFERENCE_RANGE_END)))
    answer = str(random_number)
    return question, answer
