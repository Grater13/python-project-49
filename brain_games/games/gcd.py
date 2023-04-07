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
        max_div = gcd(number1, number2)
        print('Question: ' + str(number1) + ' ' + str(number2))
        answer = prompt.string('Your answer: ')
        if str(max_div) == answer:
            print('Correct!')
        else: return print(f"""'{answer}' is wrong answer ;(. Correct answer was '{max_div}'.
Let's try again, {name}!""")
    print('Congratulations, ' + name + '!')
