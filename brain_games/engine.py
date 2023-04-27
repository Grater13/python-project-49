import prompt

NUMBER_OF_ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print(game.RULE)

    for i in range(NUMBER_OF_ROUNDS):
        question, answer = game.get_round()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != answer:
            print(f'''"{user_answer}" is wrong answer ;(. \
Correct answer was "{answer}".
Let's try again, {name}!''')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
