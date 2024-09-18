# import prompt library

import prompt

def welcome_user():
    name = prompt.string('May I have your name? ') #User must be input name by defolt else again the same question
    print(f'Hello, {name}!')



