import time
import os
import random

# Globals:
re = ("\033[0;37;41m   \033[0m") 
bl = ("\033[0;37;40m   \033[0m")
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

#######################
#    Board dolgok     #
#######################

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
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

# nagyitás:
z=2 
board2="".join([board_ai[0][0]*z, board_ai[0][1]*z])
print(board2)

def print_board():
    #ai:
        print("    ----Computer:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print(" ", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("1", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("")

    #player:
        print("    ----Player1:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print(" ", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
        print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
        print("")

def position_gen():
    # addig generáltathat a player, amig nem tetszik neki az a leosztás 
    # ha oké, akkor az ainak is legenerálódik a sajátja csak fekvőben 
    while True:  
        user_input=input("Jó ez az elrendezés? (Y/N)").lower() 
        if user_input == "y": 
            print("oké")
            time.sleep(1)
            break 
        else:
            print("Generating...")

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
    # if __hit___ ág:
    #     #a találathoz képest +/-1 cella és +-/1 row-la löjje a következő lépéseit  
    # else:
    #     random.choice(allowed_chars) #abból a listából, ami még megmaradt 
    pass

def check_hit(user_input):
    x = 'abcdef'.index(user_input[0])
    y = '123456'.index(user_input[1])

    if board_ai_ships[x][y] == 0:
        board_player[x][y] = bl
        print("Nem talált!")

def check_winning():
    global winning  
    if (sum(row.count(re) for row in board_ai)) > 1:
        print("the winner is: player 1")
        print("")
        winning = True 
        
    elif (sum(row.count(re) for row in board_player)) >= 5:
        print("the winner is: the computer")
        print("")
        winning = True 
    else:
        pass

while True:
    position_gen()
    break 

while winning == False:
    # logika jó e igy? mit kell minek átadnia hogy jó legyen?
    os.system('clear')
    print_board()
    check_hit(player_input())
    time.sleep(1)
    ai() #ő utána is kéne egy check_hit, vagy roundok kellenek
    check_winning()