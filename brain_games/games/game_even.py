# Import section
from brain_games.games.game_engine_general import get_random_number

# BEGIN

# Game rules
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


# check even/not even
def is_even(number):
    return number % 2 == 0


# common even function
def formulate_question_get_answer():
    number = get_random_number()
    question = str(number)
    if is_even(number) is True:
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return question, correct_answer


# END
