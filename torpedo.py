import time
import os
import random
import pprint

# todo : jelek, ai , position gen 

# Globals:
re = ("\033[0;37;41m  \033[0m")
bl = ("\033[0;37;40m  \033[0m")
# maradék jelek: találat, mellé, hajó1, hajó2, ai_hajó1, ai_hajó2
player1 = 1
ai = 1
winning = False
hits = []
player_hit = []
allowed_chars = ("a1", "a2", "a3", "a4", "a5",
                 "b1", "b2", "b3", "b4", "b5",
                 "c1", "c2", "c3", "c4", "c5",
                 "d1", "d2", "d3", "d4", "d5",
                 "e1", "e2", "e3", "e4", "e5",
                 "f1", "f2", "f3", "f4", "f5",
                 )
allowed_position = [(x, y) for x in range(6) for y in range(6)]
zz = 1
yy = list(range(zz))
maxlength = 1.8*zz
maxlength2 = "".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"])
space = " "
is_hit = False    
ai_hits = [(2, 3), (4, 4), (1, 0), (2, 0), (3, 2), (0, 0), (5, 2), (1, 3), (1, 1)]

# Board stuff:  
board_ai = [
    [bl, bl, bl, bl, bl, bl],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

board_ai_ships = [
    [0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 3, 3],
    [0, 0, 0, 0, 0, 0],
]

board_player = [
    [re, re, re, re, re, re],
    [re, re, re, re, re, re],
    [re, re, re, re, re, re],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

# Zoom:
def print_board2():
    # ai:
    print ("Computer: \n".center(len(maxlength2)))
    print('{0:>{width}}A {0:>{width}}B {0:>{width}}C {0:>{width}}D {0:>{width}}E {0:>{width}}F'.format(space, width=maxlength))
    for i in yy:
        print("".join(["1 ", board_ai[0][0]*zz+"|", board_ai[0][1]*zz+"|", board_ai[0][2]
                       * zz+"|", board_ai[0][3]*zz+"|", board_ai[0][4]*zz+"|", board_ai[0][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
    for i in yy:
        pass
        #print("".join(["2 ", board_ai[1][0]*z+"|", board_ai[1][1]*z+"|"]))
    print("")

def print_board():
    #ai:
        print("    ----Computer:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print("1", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("2", board_ai[1][0], board_ai[1][1], board_ai[1][2], board_ai[1][3], board_ai[1][4], board_ai[1][5], sep="")
        print("3", board_ai[2][0], board_ai[2][1], board_ai[2][2], board_ai[2][3], board_ai[2][4], board_ai[2][5], sep="")
        print("4", board_ai[3][0], board_ai[3][1], board_ai[3][2], board_ai[3][3], board_ai[3][4], board_ai[3][5], sep="")
        print("5", board_ai[4][0], board_ai[4][1], board_ai[4][2], board_ai[4][3], board_ai[4][4], board_ai[4][5], sep="")
        print("6", board_ai[5][0], board_ai[5][1], board_ai[5][2], board_ai[5][3], board_ai[5][4], board_ai[5][5], sep="")
        print("")

    #player:
        print("    ----Player1:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
        print("2", board_player[1][0], board_player[1][1], board_player[1][2], board_player[1][3], board_player[1][4], board_player[1][5], sep="")
        print("3", board_player[2][0], board_player[2][1], board_player[2][2], board_player[2][3], board_player[2][4], board_player[2][5], sep="")
        print("4", board_player[3][0], board_player[3][1], board_player[3][2], board_player[3][3], board_player[3][4], board_player[3][5], sep="")
        print("5", board_player[4][0], board_player[4][1], board_player[4][2], board_player[4][3], board_player[4][4], board_player[4][5], sep="")
        print("6", board_player[5][0], board_player[5][1], board_player[5][2], board_player[5][3], board_player[5][4], board_player[5][5], sep="")
        print("")

def player_input():
    while True:  
        user_input=input("target?").lower() #loweresitjük, hogy ne kelljen annyi félét nézni
        if user_input in hits: 
            print("már volt")
        elif user_input in allowed_chars:
            print("ok")
            hits.append(user_input)
            return user_input
            break
        else: 
            print("wrong format")

def ai():
    global is_hit
    #global ai_hits
    if is_hit == True:
        last_shot = ai_hits[-1] 
        x = last_shot[0]
        y = last_shot[1]
        if x+1 < len(board_player):
            board_player[x+1][y] = bl 
            ai_hits.append((x+1,y))
            # kéne check, hogy talált-e ás hogy kell-e állitani az is_hit-et 
        else:
            board_ai[x-2][y] = bl
            ai_hits.append((x-2,y))
    else:
        shot = random.choice(allowed_position) 
        x = shot[0]
        y = shot[1]
        while shot in ai_hits:
            shot = random.choice(allowed_position) 
            print("....")
        if board_player[x][y] == re:
            board_player[x][y] = 0 
            is_hit = True 
            ai_hits.append(shot)
            print("talált")
            time.sleep(2)
        else:
            board_player[x][y] = re 
            ai_hits.append(shot)
        print(is_hit)
        time.sleep(1)

def check_hit(user_input):
    y = 'abcdef'.index(user_input[0])
    x = '123456'.index(user_input[1])

    print(board_ai_ships[x][y])
    if board_ai_ships[x][y] == 0:
        board_ai[x][y] = re
        #pprint.pprint(board_ai)
        print("Nem talált!")

def check_winning():
    global winning  
    if (sum(row.count(re) for row in board_ai)) > 6:
        print("the winner is: player 1")
        print("")
        winning = True 
        
    elif (sum(row.count(re) for row in board_player)) >= 45:
        print("the winner is: the computer")
        print("")
        winning = True 
    else:
        pass

def position_gen():
    allowed_chars = [(x, y) for x in range(6) for y in range(6)]
    board_ai = [[0 for x in range(6)] for y in range(6)]

    elso_hajo = random.choice(allowed_chars)
    print(elso_hajo)
    # place ship:
    x = elso_hajo[0]
    y = elso_hajo[1]
    board_ai[x][y] = 2  

    if x+2 < len(board_ai):
        board_ai[x+2][y] = 2
        board_ai[x+1][y] = 2
        allowed_chars.remove((x+1,y))
        allowed_chars.remove((x+2,y))
    else:
        board_ai[x-2][y] = 2
        board_ai[x-1][y] = 2
        allowed_chars.remove((x-1,y))
        allowed_chars.remove((x-2,y))
        
    allowed_chars.remove(elso_hajo)

    # print(allowed_chars)
    # print("")

    masodik_hajo = random.choice(allowed_chars)
    print(masodik_hajo)
    x = masodik_hajo[0]
    y = masodik_hajo[1]
    board_ai[x][y] = 2  

    if y+1 < len(board_ai):
        board_ai[x][y+1] = 2
        #allowed_chars.remove((x,y+1))
    else:
        board_ai[x][y-1] = 2
        #allowed_chars.remove((x,y-1))
    
    # kéne két return egy tábla a playernek és egy az ai-nak 
    pprint.pprint(board_ai)

# while True:
#     position_gen()
#     start_choice = input("Press '1' to start with this board or press '2' to generate a new layout")
#     if start_choice == "1":
#         break        
#     else:
#         position_gen() 

while winning == False:
    #os.system('clear')
    print_board()
    check_hit(player_input())
    time.sleep(1)
    ai() 
    #check_winning()