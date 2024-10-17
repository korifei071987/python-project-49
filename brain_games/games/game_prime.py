# import section
from brain_games.games.game_engine_general import get_random_number
# BEGIN
# Game rules


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# valid/ non-valid prime


def is_prime(number):
    devide = 1
    count = 0
    while number >= devide:
        if number % devide == 0:
            count += 1
        devide += 1
    if count >= 3:

        return 'yes'

    return 'no'


# common prime function


def formulate_question_get_answer():
    number = get_random_number()
    question = str(number)
    correct_answer = is_prime(number)

    return question, str(correct_answer)


# END
