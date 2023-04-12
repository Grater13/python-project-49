from random import randint
from random import choice
from brain_games import engine

test = 'What is the result of the expression?'


def game_logic():
    expression = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = f'{number1} {choice(expression)} {number2}'
    answer = str(eval(question))
    return question, answer


def start():
    engine.game_engine(game_logic, test)
