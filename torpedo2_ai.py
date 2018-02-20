import time
import os
import random
import pprint

# Globals:

re = ("\033[0;37;41m  \033[0m")
bl = ("\033[0;37;40m  \033[0m")
gr = ("\033[0;37;42m  \033[0m") 
bu = ("\033[0;37;44m  \033[0m")
winning = False
is_hit = False  
hits = []
player_hit = []
ai_hits = [(1, 1)]
allowed_chars = ("a1", "a2", "a3", "a4", "a5", "a6",
                 "b1", "b2", "b3", "b4", "b5", "b6",
                 "c1", "c2", "c3", "c4", "c5", "c6",
                 "d1", "d2", "d3", "d4", "d5", "d6",
                 "e1", "e2", "e3", "e4", "e5", "e6",
                 "f1", "f2", "f3", "f4", "f5", "f6",
                 )
allowed_position = [(x, y) for x in range(6) for y in range(6)]
zz = 1
yy = list(range(zz))
maxlength = 1.8*zz
maxlength2 = "".join(["  ", ("--"*zz+"-")*6])
space = " "
score = 0

game_param = {
    "points": 0,
    "points_to_add": 0,
    "game_over": False,
    "win": False,
    "high_score": 0,
    "size": 0
    }

# Board stuff:  

board_ai = [
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
]

board_ai_ships = [
    [0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0],
]

board_player = [
    [bl, gr, bl, bl, bl, bl],
    [bl, re, bl, bl, bl, bl],
    [bl, gr, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
    [bl, bl, bl, bl, bl, bl],
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
        print("score:",score)

def player_input():
    while True:  
        user_input=input("What is your target? ").lower()
        if user_input in hits: 
            print("Already shot there!")
        elif user_input in allowed_chars:
            #print("ok")
            hits.append(user_input)
            return user_input
            break
        else: 
            print("Wrong format!")


def ai_shot(x,y):
    global score
    if board_player[x][y] == bl:
        board_player[x][y] = bu
        ai_hits.append((x,y))
        print("Miss...")
    elif board_player[x][y] == gr:
        board_player[x][y] = re
        ai_hits.append((x,y))
        score -= 1 
        print("Hit")
        time.sleep(1)
    else:
        raise("ai_shot")
        
def ai():
    global is_hit
    #global ai_hits
    print("Computer's turn")
    time.sleep(2)

    last_shot = ai_hits[-1] 
    x2 = last_shot[0]
    y2 = last_shot[1]
    if board_player[x2][y2] == re: 
        if x2+1 < len(board_player):
            ai_shot(x2+1, y2)
        else:
            ai_shot(x2-1, y2)
    else:
        shot = random.choice(allowed_position) 
        x = shot[0]
        y = shot[1] #az abc  
        abc = "ABCDEF" 
        print(abc[y],x+1)

        time.sleep(1)
        while shot in ai_hits:
            shot = random.choice(allowed_position) 
            print("....")
        ai_shot(x, y)

        time.sleep(1)

def check_hit(user_input):
    y = 'abcdef'.index(user_input[0])
    x = '123456'.index(user_input[1])
    global score

    if board_ai_ships[x][y] == 0:
        board_ai[x][y] = bu
        print("Miss!")
    elif board_ai_ships[x][y] == 2:
        board_ai[x][y] = re
        print("Hit!!")  
        score += 1 

def check_winning():
    global winning  
    if (sum(row.count(re) for row in board_ai)) > 4:
        print("The winner is: player 1")
        print("")
        winning = True 
        
    elif (sum(row.count(re) for row in board_player)) >= 6:
        print("The winner is: the computer")
        print("")
        winning = True 
    else:
        pass

def position_gen():
    os.system('clear')
    global board_player
    allowed_chars = [(x, y) for x in range(6) for y in range(6)]
    board_player = [[bl for x in range(6)] for y in range(6)]

    first_ship = random.choice(allowed_chars)
    x = first_ship[0]
    y = first_ship[1]
    board_player[x][y] = gr  

    if x+2 < len(board_player):
        board_player[x+2][y] = gr
        board_player[x+1][y] = gr
        allowed_chars.remove((x+1,y))
        allowed_chars.remove((x+2,y))
    else:
        board_player[x-2][y] = gr
        board_player[x-1][y] = gr
        allowed_chars.remove((x-1,y))
        allowed_chars.remove((x-2,y))
        
    allowed_chars.remove(first_ship)

    second_ship = random.choice(allowed_chars)

    x = second_ship[0]
    y = second_ship[1]
    board_player[x][y] = gr  

    if y+1 < len(board_player):
        board_player[x][y+1] = gr
        #allowed_chars.remove((x,y+1))
    else:
        board_player[x][y-1] = gr
        #allowed_chars.remove((x,y-1))
 
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

while True:
    position_gen()
    start_choice = input("Press '1' to start with this board or press '2' to generate a new layout\n")
    if start_choice == "1":
        break        
    else:
        position_gen() 

while winning == False:
    os.system('clear')
    print_board()
    check_hit(player_input())
    time.sleep(1)
    os.system('clear')
    print_board()
    ai() 
    check_winning()