import random

# Game rules
DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def question_type(number1, number2, symbol):
    try:
        match symbol:
            case '+':
                return number1 + number2
            case '-':
                return number1 - number2
            case '*':
                return number1 * number2
    except (ValueError, SyntaxError):
        print("Use +, - or * only!")
        


def formulate_question_get_answer():
    number1, number2 = random.randint(1, 100), random.randint(1, 100)
    symbol = random.choice(OPERATORS)
    question = f"{number1} {symbol} {number2}"
    correct_answer = question_type(number1, number2, symbol)

    return question, str(correct_answer)
