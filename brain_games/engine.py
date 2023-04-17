import prompt


def game_engine(game_logic, TEST):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print(TEST)

    for i in range(3):
        question, answer = game_logic()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != str(answer):
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{answer}".
Let's try again, {name}!''')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
