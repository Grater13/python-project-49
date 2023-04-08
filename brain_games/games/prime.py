import prompt
from random import randint


def brain_prime():
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

        if counter <= 1 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return
        elif counter > 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
