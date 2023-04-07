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
        crct_ans = eval(given_number)
        print('Question: ' + str(given_number))
        ans = prompt.string('Your answer: ')

        if ans == str(crct_ans):
            print('Correct!')

        else: return print(f"""'{ans}' is wrong answer ;(. Correct answer was '{crct_ans}'.
Let's try again, {name}!""")
    print(f'Congratulations, {name}!')
