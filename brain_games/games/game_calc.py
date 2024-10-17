# import section
import random
from brain_games.games.game_engine_general import get_random_number
# BEGIN

# Game rules
DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


# type of question
def question_type(number1, number2, symbol):
    match symbol:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2


# main game function


def formulate_question_get_answer():
    number1, number2 = get_random_number(), get_random_number()
    symbol = random.choice(OPERATORS)
    question = f"{number1} {symbol} {number2}"
    correct_answer = question_type(number1, number2, symbol)

    return question, str(correct_answer)


# END
