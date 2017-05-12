import random
from time import sleep
import os

RED = '\033[31m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'

def create_board(file='diagon_alley'):
    '''OPEN AND READ MAP'''
    with open(file, 'r') as level:
        level = level.readlines()

    RED_CHARS = ['&', '|']
    BLUE_CHARS = ['[', ']', 'x']
    YELLOW_CHARS = [
        '>', '<', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'W', 'Y', 'Z']
    GREEN_CHARS = ['o', '\', ''', '!', '_', '%', 'w']

    board = []
    for row in level:
        board_row = []
        for char in row:
            if char in RED_CHARS:
                red = (RED + char + RESET)
                board_row.append(red)
            elif char in YELLOW_CHARS:
                yellow = (YELLOW + char + RESET)
                board_row.append(yellow)
            elif char in BLUE_CHARS:
                blue = (BLUE + char + RESET)
                board_row.append(blue)
            elif char in GREEN_CHARS:
                green = (GREEN + char + RESET)
                board_row.append(green)
            else:
                board_row.append(char)

        board.append(board_row)
    return board