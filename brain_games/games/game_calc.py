# import section
import prompt
import random
from brain_games.cli import welcome_user

# BEGIN
# finished game with pass result three times


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

# type of question


def question_type(count, number1, number2):
    if 0 <= count < 1:
        question = f'{number1}+{number2}'
        result = number1 + number2
        print('Question: ', question)
        return result
    elif 1 <= count < 2:
        question = f'{number1}-{number2}'
        print('Question: ', question)
        result = number1 - number2
        return result
    elif 2 <= count <= 3:
        question = f'{number1} * {number2}'
        print('Question: ', question)
        result = number1 * number2
        return result

# main game function


def game_calculate():
    count = 0
    name = welcome_user()
    print('What is the result of the expression?')
    while True:
        number1, number2 = numbers()
        result = question_type(count, number1, number2)
        answer = prompt.integer('Your answer: ')
        if correct_answer(result, answer) is True:
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again,{name}")
            break
        if count == 3:
            congratulations()
            break


# END
