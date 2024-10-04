# import section
import random
import prompt
from brain_games.games.game_engine_general import welcome_user
from brain_games.games.game_engine_general import numbers
from brain_games.games.game_engine_general import correct_answer
from brain_games.games.game_engine_general import congratulations

# BEGIN
# result of greatest common divisor between two numbers


def gcd_result(number1, number2):
    start_number = 1
    max_number = 0
    while number1 >= start_number:
        if number1 % start_number == 0 and number2 % start_number == 0:
            max_number = start_number
        start_number += 1
    result = max_number
    return result

# main gcd function


def gcd_main():
    count = 0
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while True:
        number1, number2 = numbers()
        result = gcd_result(number1, number2)
        print('Questuon:', number1, number2)
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
