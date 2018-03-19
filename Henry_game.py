from __future__ import print_function
import getch
import random
import time
import os

os.system('setterm -cursor off')

board = []

color = []

game_param = {
    "points": 0,
    "points_to_add": 0,
    "game_over": False,
    "win": False,
    "high_score": 0,
    "size": 0
    }


def initalize(game_param, board):
    
    os.system("clear")

    print("Select board size! (3-9)")
    while True:
        input = getch.getch()
        try:
            while int(input) < 3 or int(input) > 10:       
                input = getch.getch()
            break
        except:
            continue

    game_param['size'] = int(input)   

    print("Do you want to start a new game or continue? (n/c)")
    input = getch.getch()
    while input != 'c' and input != 'n':
        input = getch.getch()

    return input


def load(game_param, board, input):
    with open(str(game_param['size'])+".txt", "r") as file:
        file_content = file.read()
        file_content = file_content.split("\n")

    game_param['high_score'] = int(file_content[0])

    if input == "c":
        game_param['points'] = int(file_content[1])
        i = 0
        j = 0
        for nums in file_content[2:]:
            board[i][j] = int(nums)
            j += 1
            if j % game_param['size'] == 0:
                j = 0
                i += 1


def left(board, game_param):
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[i][j] != 0 and j < game_param['size']-1:
                nextnum = j + 1
                while board[i][nextnum] == 0:
                    if nextnum < game_param['size']-1:
                        nextnum += 1
                    else:
                        break
                if board[i][j] == board[i][nextnum] and board[i][nextnum] != 0:
                    board[i][j] *= 2
                    game_param['points_to_add'] += board[i][j]
                    board[i][nextnum] = 0
            prevnum = 0
            while board[i][prevnum] != 0 and prevnum < j:
                if prevnum < game_param['size']-1:
                    prevnum += 1
                else:
                    break
            if prevnum != j:
                board[i][prevnum] = board[i][j]
                board[i][j] = 0


def right(board, game_param):
    for i in range(game_param['size']-1, -1, -1):
        for j in range(game_param['size']-1, -1, -1):
            if board[i][j] != 0 and j > 0:
                nextnum = j - 1
                while board[i][nextnum] == 0:
                    if nextnum > 0:
                        nextnum -= 1
                    else:
                        break
                if board[i][j] == board[i][nextnum] and board[i][nextnum] != 0:
                    board[i][j] *= 2
                    game_param['points_to_add'] += board[i][j]
                    board[i][nextnum] = 0
            prevnum = game_param['size']-1
            while board[i][prevnum] != 0 and prevnum > j:
                if prevnum > 0:
                    prevnum -= 1
                else:
                    break
            if prevnum != j:
                board[i][prevnum] = board[i][j]
                board[i][j] = 0


def up(board, game_param):
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[j][i] != 0 and j < game_param['size']-1:
                nextnum = j + 1
                while board[nextnum][i] == 0:
                    if nextnum < game_param['size']-1:
                        nextnum += 1
                    else:
                        break
                if board[j][i] == board[nextnum][i] and board[nextnum][i] != 0:
                    board[j][i] *= 2
                    game_param['points_to_add'] += board[j][i]
                    board[nextnum][i] = 0
            prevnum = 0
            while board[prevnum][i] != 0 and prevnum < j:
                if prevnum < game_param['size']-1:
                    prevnum += 1
                else:
                    break
            if prevnum != j:
                board[prevnum][i] = board[j][i]
                board[j][i] = 0


def down(board, game_param):
    for i in range(game_param['size']-1, -1, -1):
        for j in range(game_param['size']-1, -1, -1):
            if board[j][i] != 0 and j > 0:
                nextnum = j - 1
                while board[nextnum][i] == 0:
                    if nextnum > 0:
                        nextnum -= 1
                    else:
                        break
                if board[j][i] == board[nextnum][i] and board[nextnum][i] != 0:
                    board[j][i] *= 2
                    game_param['points_to_add'] += board[j][i]
                    board[nextnum][i] = 0
            prevnum = game_param['size']-1
            while board[prevnum][i] != 0 and prevnum > j:
                if prevnum > 0:
                    prevnum -= 1
                else:
                    break
            if prevnum != j:
                board[prevnum][i] = board[j][i]
                board[j][i] = 0


def colorize(board, color, game_param):
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[i][j] == 0:
                color[i][j] = 47
            elif board[i][j] <= 4:
                color[i][j] = 40
            elif board[i][j] <= 16:
                color[i][j] = 45
            elif board[i][j] <= 64:
                color[i][j] = 41
            elif board[i][j] <= 256:
                color[i][j] = 43
            elif board[i][j] <= 512:
                color[i][j] = 46
            elif board[i][j] <= 1024:
                color[i][j] = 44
            elif board[i][j] <= 2048:
                color[i][j] = 42


def print_board(board, game_param):

    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[i][j] == 0:
                board[i][j] = " "
    
    os.system("clear")

    print("\033[2;30;47m Board size: " + str(game_param['size']) 
        + "  \tPoints: " + str(game_param['points']) 
        + "  \tHigh Score: " + str(game_param['high_score'])
        + " \033[0;0;0m\n")
    
    for i in range(game_param['size']):

        for k in range(game_param['size']):
            print("\033[1;37;"+str(color[i][k])+"m\t\033[0;0;0m", end="")
        print("\n", end="")

        for k in range(game_param['size']):
            print("\033[1;37;" +str(color[i][k]) +"m   " +str(board[i][k]) + "\t\033[0;0;0m", end="")
        print("\n", end="")

        for k in range(game_param['size']):
            print("\033[1;37;"+str(color[i][k])+"m\t\033[0;0;0m", end="")
        print("\n", end="")
        

    print("\n" * 7)
    print("\033[1;30;40m Controlls: w,a,s,d. Press q to quit.\033[0;0;0m")

    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[i][j] == " ":
                board[i][j] = 0


def randomize(board, game_param):
    row_0 = []
    column_0 = []
    for i in range(0, game_param['size']):
        for j in range(0, game_param['size']):
            if board[i][j] == 0:
                row_0.append(i)
                column_0.append(j)

    if len(row_0) > 1:
        random_index = random.randrange(0, len(row_0) - 1)
        board[row_0[random_index]][column_0[random_index]] = random.randrange(2, 5, 2)

    else:
        board[row_0[0]][column_0[0]] = random.randrange(2, 5, 2)


def compare_board(list_1, list_2, boolean, game_param):
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if list_1[i][j] != list_2[i][j]:
                boolean = False
    return boolean


def copy_board(paste_into_this_board, copy_this_board, game_param):
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            paste_into_this_board[i][j] = copy_this_board[i][j]


def game_over(board, game_param):
    game_over = True

    board_copy = [[0 for i in range(game_param['size'])] for i in range(game_param['size'])]

    copy_board(board_copy, board, game_param)

    up(board_copy, game_param)
    game_over = compare_board(board, board_copy, game_over, game_param)
    copy_board(board_copy, board, game_param)

    down(board_copy, game_param)
    game_over = compare_board(board, board_copy, game_over, game_param)
    copy_board(board_copy, board, game_param)

    left(board_copy, game_param)
    game_over = compare_board(board, board_copy, game_over, game_param)
    copy_board(board_copy, board, game_param)

    right(board_copy, game_param)
    game_over = compare_board(board, board_copy, game_over, game_param)
    copy_board(board_copy, board, game_param)

    return game_over


def win(board):
    for row in board:
        for column in row:
            if column == 2048:
                return True
    return False


input = initalize(game_param, board)

board = [[0 for i in range(game_param['size'])] for i in range(game_param['size'])]
color = [[40 for i in range(game_param['size'])] for i in range(game_param['size'])]

load(game_param, board, input)

randomize(board, game_param)
colorize(board, color, game_param)
print_board(board, game_param)

board2 = [[0 for i in range(game_param['size'])] for i in range(game_param['size'])]

input = getch.getch()



while input != "q" and not game_param['game_over']:

    game_param['points_to_add'] = 0

    copy_board(board2, board, game_param)

    if input == "w":
        up(board, game_param)
    elif input == "a":
        left(board, game_param)
    elif input == "s":
        down(board, game_param)
    elif input == "d":
        right(board, game_param)

    game_param['points'] += game_param['points_to_add']
    if game_param['points'] > game_param['high_score']:
        game_param['high_score'] = game_param['points']

    colorize(board, color, game_param)
    print_board(board, game_param)

    randomboard = True
    for i in range(game_param['size']):
        for j in range(game_param['size']):
            if board[i][j] != board2[i][j] and randomboard:
                randomize(board, game_param)
                randomboard = False

    time.sleep(0.1)

    game_param['game_over'] = game_over(board, game_param)
    game_param['win'] = win(board)

    colorize(board, color, game_param)
    print_board(board, game_param)
    input = getch.getch()

if game_param['win']:
    print(
        "\033[2;30;47m You win!\t\033[0;0;0m\n\033[2;30;47m Points: " +
        str(game_param['points']) +
        "\t\033[0;0;0m")
    board = [[0 for i in range(game_param['size'])] for i in range(game_param['size'])]
elif game_param['game_over']:
    print(
        "\033[2;30;47m Game over!\t\033[0;0;0m\n\033[2;30;47m Points: " +
        str(game_param['points']) +
        "\t\033[0;0;0m")
    board = [[0 for i in range(game_param['size'])] for i in range(game_param['size'])]

with open(str(game_param['size'])+".txt", "w") as file:
    file.writelines(str(game_param['high_score']))
    file.writelines("\n"+str(game_param['points']))
    for row in board:
        for column in row:
            file.writelines("\n"+str(column))
    