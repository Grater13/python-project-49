import prompt
from random import randint
from math import gcd


def brain_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        m_div = gcd(number1, number2)
        print('Question: ' + str(number1) + ' ' + str(number2))
        ans = prompt.string('Your answer: ')
        if str(m_div) == ans:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{m_div}'.")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')
