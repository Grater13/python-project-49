import prompt
from random import randint
from math import gcd

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        max_divider = gcd(number1, number2)
        print('Question: ' + str(number1) + ' ' + str(number2))
        answer = prompt.string('Your answer: ')
        if str(max_divider) == answer:
            print('Correct!')
        else: return print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + "'" + str(max_divider) + "'.\nLet's try again, " + name + "!")
    print('Congratulations, ' + name + '!')
