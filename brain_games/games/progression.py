from random import randint

TEST = 'What number is missing in the progression?'
POSITIONS_IN_LINE = 11
RANGE_START = 2
INITIAL_ELEM_RANGE_END = 60
COMMON_DIFF_RANGE_END = 6


def progression_line():
    initial_element = randint(RANGE_START, INITIAL_ELEM_RANGE_END)
    common_difference = randint(RANGE_START, COMMON_DIFF_RANGE_END)
    previous_element = initial_element
    line = []
    for n in range(POSITIONS_IN_LINE):
        current_element = previous_element + common_difference
        previous_element = current_element
        line.append(current_element)
    return line


HID_ELEM_POS_START = 0
HID_ELEM_POS_END = 9


def question_string():
    line = progression_line()
    random_position = randint(HID_ELEM_POS_START, HID_ELEM_POS_END)
    hidden_number = line[random_position]
    line[random_position] = '..'
    question = ' '.join(map(str, line))
    return question, hidden_number


def question_answer_return():
    question, hidden_number = question_string()
    answer = str(hidden_number)
    return question, answer
