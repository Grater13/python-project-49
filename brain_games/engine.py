import prompt


def game_engine(game_logic, test):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print(test)

    for i in range(3):
        question, answer = game_logic()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) != str(answer):
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{answer}".
Let's try again, {name}!''')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
