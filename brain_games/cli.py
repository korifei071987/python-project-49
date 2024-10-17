# import prompt library
import prompt


# BEGIN


def welcome_user():
    # User must be input name by defolt
    name = prompt.string(
        'Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name
# END
