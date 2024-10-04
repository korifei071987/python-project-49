# import section
import random
import prompt
from brain_games.games.game_engine_general import welcome_user
from brain_games.games.game_engine_general import numbers
from brain_games.games.game_engine_general import correct_answer
from brain_games.games.game_engine_general import congratulations
from brain_games.games.game_even import is_valid_answer

# BEGIN
# generation one random number


def random_number():
    number = random.randint(1, 100)
    return number

# valid/ non-valid prime


def is_prime(number):
    devide = 1
    count = 0
    while number >= devide:
        if number % devide == 0:
            count += 1
        devide += 1
    if count >= 3:
        return False
    return True

# common game function


def main_prime():
    count = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while True:
        number = random_number()
        print('Questuon:', number)
        answer = prompt.string('Your answer: ')
        if is_prime(number) == True:
            result = 'yes'
        else:
            result = 'no'
        if is_valid_answer(answer) is True and correct_answer(result, answer) is True:
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again, {name}")
            break
        if count == 3:
            congratulations()
            break


# END
