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


# common progression function

def formulate_question_get_answer():
    list_numbers = progression()
    random_index = random.randint(2, len(list_numbers) - 1)
    correct_answer = list_numbers[random_index]
    list_numbers[random_index] = '..'
    question = ' '.join(map(str, list_numbers))

    return question, str(correct_answer)
