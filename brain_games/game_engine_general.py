import random
import prompt


# Rounds

ATTEMPTS_COUNT = 3


# Game engine

def run_game(game_name):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_name.DESCRIPTION)
    for i in range(ATTEMPTS_COUNT):
        question, correct_answer = game_name.formulate_question_get_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
        print("Correct!")
    else:
        print("Congratulations!")
