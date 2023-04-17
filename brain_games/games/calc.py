from random import randint
from random import choice

TEST = 'What is the result of the expression?'


def game_logic():
    expression = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = f'{number1} {choice(expression)} {number2}'
    answer = eval(question)
    return question, str(answer)
