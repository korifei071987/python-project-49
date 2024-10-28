import random

# Game rules
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# valid/ non-valid prime
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def formulate_question_get_answer():
    number = random.randint(1, 100)
    question = str(number)
    value = is_prime(number)
    correct_answer = 'yes' if value else 'no'

    return question, str(correct_answer)
