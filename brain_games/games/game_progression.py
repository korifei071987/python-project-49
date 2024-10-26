# import section
import random

# Game rules
DESCRIPTION = 'What number is missing in the progression?'


# function for inicialization and generation arithmetic progression

def progression():
    list_numbers = []
    step = random.randint(1, 10)
    number = random.randint(1, 100)
    list_numbers.append(number)
    for i in range(9):
        list_numbers.append(number + step)
        number += step

    return list_numbers


# function, which hide symbol in list

def hide_symbol(list_numbers):
    list_numbers = progression()
    hidden_index = random.randint(2, len(list_numbers) - 1)
    hidden_symbol = list_numbers.pop(hidden_index)
    list_numbers.insert(hidden_index, '..')
    result = hidden_symbol

    return list_numbers, result


# common progression function

def formulate_question_get_answer():
    list_numbers, result = hide_symbol(progression)
    question = f'{list_numbers}'
    correct_answer = result

    return question, str(correct_answer)
