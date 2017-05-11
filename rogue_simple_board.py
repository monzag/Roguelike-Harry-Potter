import random
from time import sleep
import os

RED = '\033[31m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'


def start_screen(file='start_screen'):
    '''Open file and read it'''
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


def help_screen():
    '''Help for user. Choose option and print information'''
    while True:
        print('''
        1. Movement
        2. Enemy
        3. Exit
        ''')

        try:
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

        except:
            print('Bad number')


def author_screen():
    '''Information about authors'''
    text = ('''
    Two strong and independent womens. With cats and broomstricks.
    Like witches from Harry Potter. Now you know our inspiration;)''')
    return text


def menu_choose(menu):
    '''Choice options of menu'''
    try:
        menu = int(input('Chose 1, 2, 3 '))
        if menu == 1:
            show_character_screen()
        elif menu == 2:
            help_screen()
        elif menu == 3:
            print(author_screen())
        elif menu == 4:
            print("Return")
    except:
        print("bad")
    return menu


def start():
    '''Beginning functions like start screen, menu, information, help'''
    start_screen('start_screen')
    sleep(2)
    os.system("clear")

    menu = 1
    while menu:
        start_screen('menu_screen')
        choice_diagon = menu_choose(menu)
        if choice_diagon == 4:
            os.system("clear")
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
    '''RANDOM POSITION OF ENEMY IN SPECIFIC RANGE (DIFFRENT FOR ANOTHER BOARD).
    CHANGE PLACE WHERE ! AS EMPTY SPACE'''
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
    '''COLLECT LUGGAGE FROM LEVEL, ADD POINTS AND ITEMS TO INVENTORY'''
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


def print_inventory(board, inventory):
    '''Inventory (key, value) on the right side of board. Value aligned to the right'''
    i = 1

    for key in inventory:
        board[i][63] = key
        board[i][69] = str(inventory[key]).rjust(18-len(key))
        i += 1

    return board


def ask_puzzles(points, board, x_pos, y_pos):
    '''ASK PUZZLES AFTER TOUCH ! SIGN'''
    puzzle_position = board[y_pos][x_pos]
    collection_of_questions = {
        'What kind of spell do you use to open the locks?: HINT:a': "alohomora",
        'What is called a house with a snake symbol? HINT:S': 'slytherin',
        'What is the name of the elixir teacher? HINT:S': 'snape',
        'Who is Headmaster of Hogwart? ': 'dumbletore',
        'What is the school of Harry Potter named? HINT:H': 'hogwart',
        'What Harry has on his forehead? HINT:S': 'scar',
        'Who is the best friend of Harry (boy)? HINT:R': 'ron',
        'Who is the best friend of Harry (girl)? HINT:H': 'hermione',
        'To which house is assigned Harry? HINT: G': 'gryffindor',
        'Members of this house are characterised by their wit, learning, and wisdom. HINT:R': 'ravenclaw'
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
    '''Compare our position to spider position'''
    spider_position = board[y_pos][x_pos]
    spider = (BLUE + 'x' + RESET)
    if spider_position in spider:
        return 1


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


def game_over():
    '''display lose screen and show all scorelist'''
    import lose_screen
    import scorelist
    scorelist.display_scorelist()


def winner(points):
    '''display win screen, add data to ranking and show all scorelist'''
    import win_screen
    import scorelist
    ranking = scorelist.get_score_list(points)
    scorelist.add_result_to_scorelist(ranking)
    scorelist.display_scorelist()


def play_again(want_play):
    '''choice about next game'''
    ask = input('Do you want to play again? (y/n): ').lower()
    if ask == 'y':
        want_play = 0

    else:
        print('Good bye')
        exit()

    return want_play


def main():
    start()
    key_press = ' '

    start_play = 1
    while key_press != 'x' and start_play == 1:
        points = 0
        inventory = {'books': 0, 'wand': 0, 'bean':  0, 'elixir': 0, 'broomstick': 0, 'owl': 0, 'golden snitch': 0}

        import story_alley
        sleep(5)

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

        want_play = 1
        while key_press != 'x' and want_play == 1:
            key_press = getch().lower()
            old_x = x_pos
            old_y = y_pos
            x_pos, y_pos = user_move(x_pos, y_pos, key_press, board)
            os.system("clear")
            points, inventory = collect_item(points, board, x_pos, y_pos, inventory)
            points = ask_puzzles(points, board, x_pos, y_pos)
            final_fight = touch_spider(board, x_pos, y_pos)
            if final_fight == 1:
                guess = random_number()
                find_number(guess, points)
                want_play = play_again(want_play)

            board = insert_player(board, x_pos, y_pos, old_x, old_y)
            board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, x_from, x_to, y_from, y_to)
            print_board(board, points)
            print_inventory(board, inventory)

            if points >= 1 and level == 1:
                os.system("clear")
                import story_quidditch
                sleep(5)
                level += 1
                x_pos = 2
                y_pos = 2
                enemy_y = 21
                enemy_x = 24
                board = create_board('quidditch_game')
                board = insert_player(board, x_pos, y_pos, old_x, old_y)
                board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 24, 27, 20, 22)

            if points > 25 and level == 2:
                os.system("clear")
                import story_elixir
                sleep(5)
                level += 1
                x_pos = 2
                y_pos = 2
                enemy_y = 15
                enemy_x = 16
                board = insert_player(board, x_pos, y_pos, old_x, old_y)
                board = create_board('elixir_lesson')
                board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 15, 17, 14, 18)

            if points > 30 and level == 3:
                import story_forest
                sleep(5)
                level += 1
                x_pos = 2
                y_pos = 2
                enemy_y = 21
                enemy_x = 18
                board = insert_player(board, x_pos, y_pos, old_x, old_y)
                board = create_board('forest')
                board, enemy_y, enemy_x, x_from, x_to, y_from, y_to = insert_enemy(board, enemy_y, enemy_x, 17, 18, 21, 22)

            if points < 0:
                game_over()
                want_play = play_again(want_play)


if __name__ == '__main__':
    main()

