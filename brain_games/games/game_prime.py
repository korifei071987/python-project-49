import random

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

        return True

    return False


def formulate_question_get_answer():
    number = random.randint(1, 100)
    question = str(number)
    value = is_prime(number)
    correct_answer = 'yes' if value else 'no'

    return question, str(correct_answer)
