import prompt
from random import randint
from random import choice


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')

    for i in range(3):
        expression = ['+', '-', '*']
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        given_number = str(number1) + ' ' + str(choice(expression)) + ' ' + str(number2)
        correct_answer = eval(given_number)
        print('Question: ' + str(given_number))
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')

        else: return print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + "'" + str(correct_answer) + "'.\nLet's try again, " + name + "!")
    print('Congratulations, ' + name + '!')
