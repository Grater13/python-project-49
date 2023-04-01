import prompt
from random import randint

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = randint(1, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')

        elif number % 2 != 0 and answer == 'no':
            print('Correct!')

        elif number % 2 == 0 and answer != 'yes':
            return print('"' + answer + '"' + " is wrong answer ;(. Correct answer was \"yes\".\nLet's try again, " + name + "!")
        elif number % 2 != 0 and answer != 'no':
            return print('"' + answer + '"' + " is wrong answer ;(. Correct answer was \"no\".\nLet's try again, " + name + "!")
    print('Congratulations, ' + name + '!')

