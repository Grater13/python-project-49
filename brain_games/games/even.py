import prompt
from random import randint


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')

        if number % 2 == 0 and answer != 'yes':
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}!''')
            return
        elif number % 2 != 0 and answer != 'no':
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "no".
Let's try again, {name}!''')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
