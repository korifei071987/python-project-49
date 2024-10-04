# import section
import random
import prompt
from brain_games.games.game_engine_general import welcome_user
from brain_games.games.game_engine_general import correct_answer
from brain_games.games.game_engine_general import congratulations

# BEGIN
# function for inicialization and generation arifmetic progression


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


def hide_symbol(progression):
    list_numbers = progression()
    hidden_index = random.randint(2, 11)
    hidden_symbol = list_numbers.pop(hidden_index)
    list_numbers.insert(hidden_index, '..')
    result = hidden_symbol
    return list_numbers, result


# common game function
def main_progression():
    count = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while True:
        list_numbers, result = hide_symbol(progression)
        print('Question:', *list_numbers)
        answer = prompt.integer('Your answer: ')
        if correct_answer(result, answer) is True:
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again, {name}")
            break
        if count == 3:
            congratulations()
            break

# END
