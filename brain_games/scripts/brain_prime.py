import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(3):
        number = randint(2, 100)
        counter = 0

        for n in range(1, int(number / 2)):
            if number % n == 0:
                counter += 1

        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')

        if counter <= 1 and answer == 'yes':
            print('Correct!')
        elif counter > 1 and answer == 'no':
            print('Correct!')
        elif counter <= 1 and answer == 'no':
            return print('"' + answer + '"' + " is wrong answer ;(. Correct answer was \"yes\".\nLet's try again, " + name + "!")
        elif counter > 1 and answer == 'yes':
            return print('"' + answer + '"' + " is wrong answer ;(. Correct answer was \"no\".\nLet's try again, " + name + "!")
    print('Congratulations, ' + name + '!')
