from random import randint
from random import choice

test = 'What is the result of the expression?'


def game_logic():
    expression = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = f'{number1} {choice(expression)} {number2}'
    answer = str(eval(question))
    return question, answer
