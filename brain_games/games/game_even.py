
# BEGIN
# Import section
from random import randint
from brain_games.cli import welcome_user


# check even/not even
def is_even(number):
    if number % 2 == 0:
        return True
    return False


# check correct input answer
def is_valid_answer(answer):
    if answer.lower() == 'yes' or answer.lower() == 'no':
        return True
    return False


# main game brain_even
def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while True:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if is_valid_answer(answer) is False:
            print("This is wrong answer.")
            print('''Let's try again, ''', name)
            break
        else:
            if is_even(number) is True:
                if answer == 'no':
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                    print("Let's try again," + name + '!')
                    break
                else:
                    print('Correct!')
                    count += 1
            elif is_even(number) is False:
                if answer == 'yes':
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                    print("Let's try again," + name + '!')
                    break
                else:
                    print('Correct!')
                    count += 1
        if count == 3:
            print('Congratulations, ' + name + '!')
            break


# END
