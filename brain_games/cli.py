# import prompt library
import prompt


def welcome_user():
    # User must be input name by defolt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
