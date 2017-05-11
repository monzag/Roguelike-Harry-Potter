import random
from time import sleep
import os

RED = '\033[31m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'


def start_screen(file = 'start_screen'):
    with open(file, 'r') as screen:
        screen = screen.readlines()

    for row in screen:
        for char in row:
            print(char, end='')


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
    sleep(2)
    menu = 1
    os.system('clear')
    return menu


def menu_choose(menu):
    menu = int(input('Chose 1, 2, 3 '))
    if menu == 1:
        show_character_screen()
    elif menu == 2:
        help_screen()
    elif menu == 3:
        print("b")
    return menu


def help_screen():
    while True:
        print('''
        1. Movement
        2. Enemy
        3. Exit
        ''')

        user_choice = input("Chose a number: ")
        if user_choice == '1':
            print('''
            Harry Potter's movement: WSAD keys.
            W - up, S - down, A - left, D - right''')

        if user_choice == '2':
            print('''
            Your enemy is You-Know_who (!). Bad touch can hurt - minus 5 points!.
            ''')

        if user_choice == '3':
            break


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


def print_board(board, points):
    '''PRINT EVERY MAP'''
    for row in board:
        for char in row:
            print(char, end='')

    print("Griffindor points: ", points)


def insert_player(board, x_pos, y_pos, old_x=1, old_y=1):
    '''CHANGE PLACE WHERE @ AS EMPTY SPACE'''
    board[old_y][old_x] = ' '
    board[y_pos][x_pos] = '@'
    return board


def insert_enemy(board, enemy_y, enemy_x, range_x_from, range_x_to, range_y_from, range_y_to):
    old_y = enemy_y
    old_x = enemy_x

    enemy_x = random.randint(range_x_from, range_x_to)
    enemy_y = random.randint(range_y_from, range_y_to)

    board[old_y][old_x] = ' '
    board[enemy_y][enemy_x] = GREEN + '!' + RESET

    return board, enemy_y, enemy_x, range_x_from, range_x_to, range_y_from, range_y_to


def getch():
    import sys, tty, termios
    from select import select
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        [i, o, e] = select([sys.stdin.fileno()], [], [], 0.35)
        if i: ch = sys.stdin.read(1)
        else: ch = ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def user_move(x_pos, y_pos, key_press, board):
    '''FUNCTION WHICH MOVE OUR USER'''
    old_position_x = x_pos
    old_position_y = y_pos
    left_side_x = board[y_pos][x_pos - 1]
    right_side_x = board[y_pos][x_pos + 1]
    up_side_x = board[y_pos - 1][x_pos]
    down_side_x = board[y_pos + 1][x_pos]

    OBSTACLES = ['#', RED + '|' + RESET, '*', '-', 'X']

    if key_press == 'a' and left_side_x not in OBSTACLES:
        x_pos -= 1
    elif key_press == 'd' and right_side_x not in OBSTACLES:
        x_pos += 1
    elif key_press == 'w' and up_side_x not in OBSTACLES:
        y_pos -= 1
    elif key_press == 's' and down_side_x not in OBSTACLES:
        y_pos += 1
    else:
        x_pos = old_position_x
        y_pos = old_position_y
    return x_pos, y_pos


def collect_item(points, board, x_pos, y_pos, inventory):
    '''COLLECT LUGGAGE FROM LEVEL'''
    player_position = board[y_pos][x_pos]
    items = {
            YELLOW + 'I' + RESET: 0.25, RED + '&' + RESET: 0.5, GREEN + 'w' + RESET: 2,
            BLUE + '[' + RESET: 1, BLUE + ']' + RESET: 1, YELLOW + '>' + RESET: 3,
            GREEN + '!' + RESET: -5, YELLOW + 'O' + RESET: 25, GREEN + '%' + RESET: 1
            }

    if player_position in items:
        points += items[player_position]
    if player_position == BLUE + '[' + RESET or player_position == BLUE + ']' + RESET:
        inventory['books'] += 1
    if player_position == YELLOW + 'I' + RESET:
        inventory['wand'] += 1
    if player_position == RED + '&' + RESET:
        inventory['bean'] += 1
    if player_position == GREEN + 'w' + RESET:
        inventory['owl'] += 1
    if player_position == YELLOW + '>' + RESET:
        inventory['broomstick'] += 1
    if player_position == YELLOW + 'O' + RESET:
        inventory['golden snitch'] += 1
    if player_position == GREEN + '%' + RESET:
        inventory['elixir'] += 1

    return points, inventory


def ask_puzzles(points, board, x_pos, y_pos):
    '''ASK PUZZLES AFTER TOUCH ! SIGN'''
    puzzle_position = board[y_pos][x_pos]
    collection_of_questions = {
        'What kind of spell do you use to open the locks?: HINT:a': "alohomora",
        'What is called a house with a snake symbol? HINT:S': 'slytherin',
        'What is the name of the elixir teacher? HINT:S': 'snape'
        }

    puzzle_items = (GREEN + '%' + RESET)

    if puzzle_position in puzzle_items:
        all_keys = collection_of_questions.keys()
        random_question = random.choice(list(all_keys))
        print(random_question)
        user_response = input('Give sth: ').lower()
        if user_response == collection_of_questions[random_question]:
            points += 3
        else:
            points -= 2
    return points


def touch_spider(board, x_pos, y_pos):
    spider_position = board[y_pos][x_pos]
    spider = (BLUE + 'x' + RESET)
    if spider_position in spider:
        guess = random_number()
        find_number(guess)


def random_number():
    while True:
        secret_numbers = random.sample(range(0, 9), 3)
        print(secret_numbers)
        if secret_numbers[0] == 0:
            print('')
        else:
            secret_number = ''.join(str(item) for item in secret_numbers)
            break
    return secret_number


def find_number(secret_number):
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
                    print('hot')
                else:
                    index += 1
                    print('warm')
            else:
                index += 1
                print('cold')
        if secret_number == user_choice:
            print('Win!!')
            # win screen
            break
        if guess == 10:
            print("Bad answer. Now I'll kill you!")
            # lose screen


def main():
    # start screen
    key_press = ' '
    points = 0
    points = 0
    inventory = {'books': 0, 'wand': 0, 'bean':  0, 'elixir': 0, 'broomstick': 0, 'owl': 0, 'golden snitch': 0}

    start_screen('start_screen')
    sleep(2)
    os.system("clear")

    menu = 1
    while menu:
        start_screen('menu_screen')
        choice_diagon = menu_choose(menu)
        if choice_diagon == 3:
            os.system("clear")
            break
    board = create_board()

    x_pos = 15
    y_pos = 5
    enemy_x = 12
    enemy_y = 10
    x_from = 12
    x_to = 17
    y_from = 10
    y_to = 12
    key_press = ' '
    level = 1

    while key_press != 'x':
        key_press = getch().lower()
        old_x = x_pos
        old_y = y_pos
        x_pos, y_pos = user_move(x_pos, y_pos, key_press, board)
        os.system("clear")
        points, inventory = collect_item(points, board, x_pos, y_pos, inventory)
        print(inventory)
        points = ask_puzzles(points, board, x_pos, y_pos)
        touch_spider(board, x_pos, y_pos)
        board = insert_player(board, x_pos, y_pos, old_x, old_y)
        board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, x_from, x_to, y_from, y_to)
        print_board(board, points)

        if points >= 3 and level == 1:
            print('Next level: quidditch')
            level += 1
            x_pos = 2
            y_pos = 2
            enemy_y = 21
            enemy_x = 24
            board = create_board('quidditch_game')
            board = insert_player(board, x_pos, y_pos, old_x, old_y)
            board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 24, 27, 20, 22)

        if points > 25 and level == 2:
            print('Next level: elixir')
            level += 1
            x_pos = 2
            y_pos = 2
            enemy_y = 15
            enemy_x = 16
            board = insert_player(board, x_pos, y_pos, old_x, old_y)
            board = create_board('elixir_lesson')
            board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 15, 17, 14, 18)

        if points > 30 and level == 3:
            print('Next level: forbidden forest')
            level += 1
            x_pos = 2
            y_pos = 2
            enemy_y = 21
            enemy_x = 18
            board = insert_player(board, x_pos, y_pos, old_x, old_y)
            board = create_board('forest')
            board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 17, 18, 21, 22)

    exit()

main()
