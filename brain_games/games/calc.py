from random import randint
from random import choice

RULE = 'What is the result of the expression?'
START_OF_THE_RANGE = 1
END_OF_THE_RANGE = 10


def question_answer_return():
    expression = ['+', '-', '*']
    number1 = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    number2 = randint(START_OF_THE_RANGE, END_OF_THE_RANGE)
    question = f'{number1} {choice(expression)} {number2}'
    answer = eval(question)
    return question, str(answer)
