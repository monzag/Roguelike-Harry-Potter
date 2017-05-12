import random

RED = '\033[31m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'


def random_number():
    '''Random secret number(3 diffrent digits)'''
    while True:
        secret_numbers = random.sample(range(0, 9), 3)
        print(secret_numbers)
        if secret_numbers[0] == 0:
            print('')
        else:
            secret_number = ''.join(str(item) for item in secret_numbers)
            break
    return secret_number


def find_number(secret_number, points):
    '''Final game hot-warm-cold. User find secret number, 10 chance'''
    guess = 0
    while guess < 10:
        user_choice = str(input('If you want to come back to Hogwart guess my 3-digit number: '))
        print(secret_number)
        guess += 1
        index = 0
        for item in user_choice:
            if item in secret_number:
                if item == secret_number[index]:
                    index += 1
                    print(RED + 'hot' + RESET, end=" ")
                else:
                    index += 1
                    print(ORANGE + 'warm' + RESET, end=" ")
            else:
                index += 1
                print(BLUE + 'cold' + RESET, end=" ")
        if secret_number == user_choice:
            print('Win!!')
            winner(points)
            break

        if guess == 10:
            print("Bad answer. Now I'll kill you!")
            game_over()
            break