import prompt
from random import randint
from random import choice


def brain_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')

    for i in range(3):
        expression = ['+', '-', '*']
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        given_number = f'{number1} {choice(expression)} {number2}'
        right = eval(given_number)
        print('Question: ' + str(given_number))
        ans = prompt.string('Your answer: ')

        if ans == str(right):
            print('Correct!')

        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
