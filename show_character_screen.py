import os
from time import sleep

RED = '\033[31m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'

def show_character_screen():
    with open('character_screen', 'r') as screen:
        screen = screen.readlines()

    RED_CHARS = ['&', '|']
    BLUE_CHARS = ['[', ']', 'x']
    YELLOW_CHARS = [
        '>', '<', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'W', 'Y', 'Z']
    GREEN_CHARS = ['o', '\', ''', '!', '_', '%', 'w']

    for row in screen:
        for char in row:
            if char in RED_CHARS:
                print(RED + char + RESET, end='')
            elif char in YELLOW_CHARS:
                print(YELLOW + char + RESET, end='')
            elif char in BLUE_CHARS:
                print(BLUE + char + RESET, end='')
            elif char in GREEN_CHARS:
                print(GREEN + char + RESET, end='')
            else:
                print(char, end='')
    sleep(5)
    menu = 1
    os.system('clear')
    return menu
