from random import randint

TEST = 'What number is missing in the progression?'
POSITIONS_IN_LINE = 11
START_OF_THE_RANGE = 2
END_OF_THE_INITIAL_ELEM_RANGE = 60
END_OF_THE_COMMON_DIFF_RANGE = 6


def progression_line():
    initial_element = randint(START_OF_THE_RANGE, END_OF_THE_INITIAL_ELEM_RANGE)
    common_difference =
    randint(START_OF_THE_RANGE, END_OF_THE_COMMON_DIFF_RANGE)
    previous_element = initial_element
    line = []
    for n in range(POSITIONS_IN_LINE):
        current_element = previous_element + common_difference
        previous_element = current_element
        line.append(current_element)
    return line


HIDDEN_ELEM_POSITION_START = 0
HIDDEN_ELEM_POSITION_END = 9


def question_string():
    line = progression_line()
    random_position =
    randint(HIDDEN_ELEM_POSITION_START, HIDDEN_ELEM_POSITION_END)
    hidden_number = line[random_position]
    line[random_position] = '..'
    question = ' '.join(map(str, line))
    return question, hidden_number


def question_answer_return():
    question, hidden_number = question_string()
    answer = str(hidden_number)
    return question, answer
