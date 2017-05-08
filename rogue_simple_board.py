from random import randint
from time import sleep
import os


def create_board(width, height):
    board = []
    for row in range(0,height):
        board_row = []
        for column in range(0, width):
            if row == 0 or row == height-1:
                board_row.append("X")
            else:
                if column == 0 or column == width - 1:
                    board_row.append("X")
                else:
                    board_row.append(" ")
        board.append(board_row)
    return board


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()


def insert_player(board, x_pos, y_pos):
    board[y_pos][x_pos] = '@'
    return board


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def user_move(x_pos, y_pos, character, board):
    old_position_x = x_pos
    old_position_y = y_pos
    left_side_x = board[y_pos][x_pos - 1]
    right_side_x = board[y_pos][x_pos + 1]
    up_side_x = board[y_pos -1][x_pos]
    down_side_x =board[y_pos + 1][x_pos]

    if character == 'a' and left_side_x != "X":
        x_pos -= 1
    elif character == 'd' and right_side_x!= "X":
        x_pos += 1
    elif character == 'w' and up_side_x != "X":
        y_pos -= 1
    elif character == 's' and down_side_x != "X":
        y_pos += 1
        #return x_pos, y_pos
    else:
        x_pos = old_position_x
        y_pos = old_position_y
    return x_pos, y_pos



def main():
    x_pos = 15
    y_pos = 5
    height = 60
    width = 20
    character = ' '
    board = create_board(height, width)
    board_with_player = insert_player(board, x_pos, y_pos)
    print_board(board_with_player)
    while character != 'x':
        character = getch()
        x_pos, y_pos = user_move(x_pos, y_pos, character, board)
        print(x_pos)
        os.system("clear")
        board = create_board(height, width)
        board_with_player = insert_player(board, x_pos, y_pos)
        print_board(board_with_player)
    exit()

main()
