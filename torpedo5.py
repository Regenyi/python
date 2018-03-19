import time
import os
import random
import pprint
import pickle

# Constants:

RE = ("\033[0;37;41m  \033[0m")
BL = ("\033[0;37;40m  \033[0m")
GR = ("\033[0;37;42m  \033[0m")
BU = ("\033[0;37;44m  \033[0m")

# Globals:

ABC = ["a","b","c","d","e","f","g","h","i","j"]
NUM = ["1","2","3","4","5","6","7","8","9"]
SIZE = 6
HITS = []
PLAYER_HIT = []
AI_HITS = [(1,1)]
ALLOWED_CHARS = [i+j for i in ABC[:SIZE] for j in NUM[:SIZE]]
ALLOWED_POSITION = [(x, y) for x in range(SIZE) for y in range(SIZE)] 

game_param = {
    "winning": False,
    "gen": True, 
    "maxlength": 1.8,
    "score": 0,
    "game_over": False,
    "high_score": 0,
    "size": 0
    }

# Board stuff:

board_ai = [
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
]

board_ai_ships = [
    [0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0],
]

def print_board():
    #ai:
        print("   Computer:\n")
        print(" ", " A", " B", " C", " D", " E", " F", sep="")
        print("1", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("2", board_ai[1][0], board_ai[1][1], board_ai[1][2], board_ai[1][3], board_ai[1][4], board_ai[1][5], sep="")
        print("3", board_ai[2][0], board_ai[2][1], board_ai[2][2], board_ai[2][3], board_ai[2][4], board_ai[2][5], sep="")
        print("4", board_ai[3][0], board_ai[3][1], board_ai[3][2], board_ai[3][3], board_ai[3][4], board_ai[3][5], sep="")
        print("5", board_ai[4][0], board_ai[4][1], board_ai[4][2], board_ai[4][3], board_ai[4][4], board_ai[4][5], sep="")
        print("6", board_ai[5][0], board_ai[5][1], board_ai[5][2], board_ai[5][3], board_ai[5][4], board_ai[5][5], sep="")
        print("")

    #player:
        print("   Player1:\n")
        print(" ", " A", " B", " C", " D", " E", " F", sep="")
        print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
        print("2", board_player[1][0], board_player[1][1], board_player[1][2], board_player[1][3], board_player[1][4], board_player[1][5], sep="")
        print("3", board_player[2][0], board_player[2][1], board_player[2][2], board_player[2][3], board_player[2][4], board_player[2][5], sep="")
        print("4", board_player[3][0], board_player[3][1], board_player[3][2], board_player[3][3], board_player[3][4], board_player[3][5], sep="")
        print("5", board_player[4][0], board_player[4][1], board_player[4][2], board_player[4][3], board_player[4][4], board_player[4][5], sep="")
        print("6", board_player[5][0], board_player[5][1], board_player[5][2], board_player[5][3], board_player[5][4], board_player[5][5], sep="")
        print("")
        print("score:", game_param["score"])

def player_input():
    while True:  
        user_input=input("What is your target? ").lower()
        if user_input in HITS: 
            print("Already shot there!")
        elif user_input == "sav":
            save_game()
        elif user_input == "x":
            exit()
        elif user_input in ALLOWED_CHARS:
            HITS.append(user_input)
            return user_input
            break
        else: 
            print("Wrong format!")

def ai_shot(x,y):
    if board_player[x][y] == BL:
        board_player[x][y] = BU
        AI_HITS.append((x,y))
        print("Miss...")
    elif board_player[x][y] == GR:
        board_player[x][y] = RE
        AI_HITS.append((x,y))
        game_param["score"] -= 1 
        print("Hit")
        time.sleep(1)
    else:
        raise("ai_shot")
        
def ai():
    print("Computer's turn")
    time.sleep(2)

    last_shot = AI_HITS[-1] 
    x2 = last_shot[0]
    y2 = last_shot[1]
    if board_player[x2][y2] == RE: 
        if x2+1 < len(board_player):
            ai_shot(x2+1, y2)
        else:
            ai_shot(x2-1, y2)
    else:
        shot = random.choice(ALLOWED_POSITION) 
        x = shot[0]
        y = shot[1] #az abc  
        abc = "ABCDEF" 
        print(abc[y],x+1)

        time.sleep(1)
        while shot in AI_HITS:
            shot = random.choice(ALLOWED_POSITION) 
            print("....")
        ai_shot(x, y)

        time.sleep(1)

def check_hit(user_input):
    y = 'abcdef'.index(user_input[0])
    x = '123456'.index(user_input[1])

    if board_ai_ships[x][y] == 0:
        board_ai[x][y] = BU
        print("Miss!")
    elif board_ai_ships[x][y] == 2:
        os.system("aplay shoot.wav&")
        board_ai[x][y] = RE
        print("Hit!!")  
        game_param["score"] += 1

def check_winning():
    if (sum(row.count(RE) for row in board_ai)) > 4:
        print("The winner is: player 1")
        print("")
        game_param["winning"] = True 
        
    elif (sum(row.count(RE) for row in board_player)) >= 6:
        print("The winner is: the computer")
        print("")
        game_param["winning"] = True 
    else:
        pass

def position_gen():
    os.system('clear')
    global board_player
    ALLOWED_CHARS = [(x, y) for x in range(6) for y in range(6)]
    board_player = [[BL for x in range(6)] for y in range(6)]

    first_ship = random.choice(ALLOWED_CHARS)
    x = first_ship[0]
    y = first_ship[1]
    board_player[x][y] = GR  

    if x+2 < len(board_player):
        board_player[x+2][y] = GR
        board_player[x+1][y] = GR
        ALLOWED_CHARS.remove((x+1,y))
        ALLOWED_CHARS.remove((x+2,y))
    else:
        board_player[x-2][y] = GR
        board_player[x-1][y] = GR
        ALLOWED_CHARS.remove((x-1,y))
        ALLOWED_CHARS.remove((x-2,y))
        
    ALLOWED_CHARS.remove(first_ship)

    second_ship = random.choice(ALLOWED_CHARS)

    x = second_ship[0]
    y = second_ship[1]
    board_player[x][y] = GR  

    if y+1 < len(board_player):
        board_player[x][y+1] = GR
        #ALLOWED_CHARS.remove((x,y+1))
    else:
        board_player[x][y-1] = GR
        #ALLOWED_CHARS.remove((x,y-1))
 
    #pprint.pprint(board_player)

    print("    ----Player1:-----\n")
    print(" ", " A", " B", " C", " D", " E", " F", sep="")
    print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
    print("2", board_player[1][0], board_player[1][1], board_player[1][2], board_player[1][3], board_player[1][4], board_player[1][5], sep="")
    print("3", board_player[2][0], board_player[2][1], board_player[2][2], board_player[2][3], board_player[2][4], board_player[2][5], sep="")
    print("4", board_player[3][0], board_player[3][1], board_player[3][2], board_player[3][3], board_player[3][4], board_player[3][5], sep="")
    print("5", board_player[4][0], board_player[4][1], board_player[4][2], board_player[4][3], board_player[4][4], board_player[4][5], sep="")
    print("6", board_player[5][0], board_player[5][1], board_player[5][2], board_player[5][3], board_player[5][4], board_player[5][5], sep="")
    print("")

    return board_player

def load_game():
    with open('torpedo.sav', 'rb') as f: 
        global game_param, board_player, board_ai, board_ai_ships, HITS, PLAYER_HIT, AI_HITS
        game_param, board_player, board_ai, board_ai_ships, HITS, PLAYER_HIT, AI_HITS = pickle.load(f)
    time.sleep(0.1)

def save_game():
    with open('torpedo.sav', 'wb') as f:  
        pickle.dump([game_param, board_player, board_ai, board_ai_ships, HITS, PLAYER_HIT, AI_HITS], f)
    print("saved!")

while True:
    os.system('clear')
    load_it = input('continue previous game? Y/N: ').lower()
    if load_it == "y":
        load_game()
        game_param["gen"] = False
        time.sleep(1)
        break
    else:
        break

while game_param["gen"] == True:
    position_gen()
    start_choice = input("Press '1' to start with this board or press '2' to generate a new layout\n")
    if start_choice == "1":
        break        
    else:
        position_gen() 

while game_param["winning"] == False:
    os.system('clear')
    print_board()
    check_hit(player_input())
    time.sleep(1)
    os.system('clear')
    print_board()
    ai() 
    check_winning()