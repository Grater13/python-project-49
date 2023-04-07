import prompt
from random import randint


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')

    for i in range(3):
        first_num = randint(2, 60)
        prog = randint(2, 5)
        prev = first_num
        list = []

        for n in range(11):
            current = prev + prog
            prev = current
            list.append(current)

        random_position = randint(0, 9)
        r_num = list[random_position]
        list[random_position] = '..'

        print('Question: ' + ' '.join(map(str, list)))
        ans = prompt.string('Your answer: ')
        if ans == str(r_num):
            print('Correct!')
        else:
            print(f"""'{ans}' is wrong answer ;(. Correct answer was '{r_num}'.
Let's try again, {name}!""")
            return
    print(f'Congratulations, {name}!')
