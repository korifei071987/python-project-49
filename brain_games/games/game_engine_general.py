import random
import prompt


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    # User must be input name by defolt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congratulations():
    print('Congratulations!')


# pass/ not pass answer
def correct_answer(result, answer):
    if result == answer:
        print('Correct!')
        return True
    return False

# generation random numbers


def numbers():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return number1, number2



        
