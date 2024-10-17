# import section
from brain_games.games.game_engine_general import get_random_number
# BEGIN

# Game rules

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

# result of greatest common divisor between two numbers


def gcd_result(number1, number2):
    start_number = 1
    max_number = 0
    while number1 >= start_number:
        if number1 % start_number == 0 and number2 % start_number == 0:
            max_number = start_number
        start_number += 1
    gcd = max_number

    return gcd


# common gcd function


def formulate_question_get_answer():
    number1, number2 = get_random_number(), get_random_number()
    question = f'{number1} {number2}'
    correct_answer = gcd_result(number1, number2)

    return question, str(correct_answer)


# END
