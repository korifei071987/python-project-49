import random
import prompt

# Common phrase


def welcome_user():
    # User must be input name by defolt
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    return name

# Celebrations


def congratulations():
    print("Congratulations!")


# Generation random numbers


def get_random_number():
    return random.randint(1, 100)


# Rounds


MAXIMUM_LEVELS = 3


# Game engine


def run_game(game_name):
    name = welcome_user()
    print(game_name.DESCRIPTION)
    level = 1
    while level <= MAXIMUM_LEVELS:
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
        level += 1
    else:
        congratulations()
