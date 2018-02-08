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
ai_hits = []
allowed_chars = ("a1", "a2", "a3", "a4", "a5", "a6",
                 "b1", "b2", "b3", "b4", "b5", "b6",
                 "c1", "c2", "c3", "c4", "c5", "c6",
                 "d1", "d2", "d3", "d4", "d5", "d6",
                 "e1", "e2", "e3", "e4", "e5", "e6",
                 "f1", "f2", "f3", "f4", "f5", "f6",
                 )
allowed_position = [(x, y) for x in range(6) for y in range(6)]
zz = 2
yy = list(range(zz))
maxlength = 1.8*zz
maxlength2 = "".join(["  ", ("--"*zz+"-")*6])
space = " "


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
    [re, re, re, re, re, re],
    [re, re, re, re, re, re],
    [re, re, re, re, re, re],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

def print_board_zoom():
    # ai:
        print ("Computer: \n".center(len(maxlength2)))
        print('{0:>{width}}A {0:>{width}}B {0:>{width}}C {0:>{width}}D {0:>{width}}E {0:>{width}}F'.format(space, width=maxlength))
        for i in yy:
            print("".join(["1 ", board_ai[0][0]*zz+"|", board_ai[0][1]*zz+"|", board_ai[0][2]*zz+"|", board_ai[0][3]*zz+"|", board_ai[0][4]*zz+"|", board_ai[0][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["2 ", board_ai[1][0]*zz+"|", board_ai[1][1]*zz+"|", board_ai[1][2]*zz+"|", board_ai[1][3]*zz+"|", board_ai[1][4]*zz+"|", board_ai[1][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["3 ", board_ai[2][0]*zz+"|", board_ai[2][1]*zz+"|", board_ai[2][2]*zz+"|", board_ai[2][3]*zz+"|", board_ai[2][4]*zz+"|", board_ai[2][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["4 ", board_ai[3][0]*zz+"|", board_ai[3][1]*zz+"|", board_ai[3][2]*zz+"|", board_ai[3][3]*zz+"|", board_ai[3][4]*zz+"|", board_ai[3][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["5 ", board_ai[4][0]*zz+"|", board_ai[4][1]*zz+"|", board_ai[4][2]*zz+"|", board_ai[4][3]*zz+"|", board_ai[4][4]*zz+"|", board_ai[4][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))                      
        for i in yy:
            print("".join(["6 ", board_ai[5][0]*zz+"|", board_ai[5][1]*zz+"|", board_ai[5][2]*zz+"|", board_ai[5][3]*zz+"|", board_ai[5][4]*zz+"|", board_ai[5][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))   
        print("")

    #Player:        
        print ("Player 1: \n".center(len(maxlength2)))
        print('{0:>{width}}A {0:>{width}}B {0:>{width}}C {0:>{width}}D {0:>{width}}E {0:>{width}}F'.format(space, width=maxlength))
        for i in yy:
            print("".join(["1 ", board_player[0][0]*zz+"|", board_player[0][1]*zz+"|", board_player[0][2]*zz+"|", board_player[0][3]*zz+"|", board_player[0][4]*zz+"|", board_player[0][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["2 ", board_player[1][0]*zz+"|", board_player[1][1]*zz+"|", board_player[1][2]*zz+"|", board_player[1][3]*zz+"|", board_player[1][4]*zz+"|", board_player[1][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["3 ", board_player[2][0]*zz+"|", board_player[2][1]*zz+"|", board_player[2][2]*zz+"|", board_player[2][3]*zz+"|", board_player[2][4]*zz+"|", board_player[2][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["4 ", board_player[3][0]*zz+"|", board_player[3][1]*zz+"|", board_player[3][2]*zz+"|", board_player[3][3]*zz+"|", board_player[3][4]*zz+"|", board_player[3][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
        for i in yy:
            print("".join(["5 ", board_player[4][0]*zz+"|", board_player[4][1]*zz+"|", board_player[4][2]*zz+"|", board_player[4][3]*zz+"|", board_player[4][4]*zz+"|", board_player[4][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))                      
        for i in yy:
            print("".join(["6 ", board_player[5][0]*zz+"|", board_player[5][1]*zz+"|", board_player[5][2]*zz+"|", board_player[5][3]*zz+"|", board_player[5][4]*zz+"|", board_player[5][5]*zz+"|"]))
        print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))   
        print("")

def print_board():
    #ai:
        print("    ----Computer:-----\n")
        print(" ", " A", " B", " C", " D", " E", " F", sep="")
        print("1", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("2", board_ai[1][0], board_ai[1][1], board_ai[1][2], board_ai[1][3], board_ai[1][4], board_ai[1][5], sep="")
        print("3", board_ai[2][0], board_ai[2][1], board_ai[2][2], board_ai[2][3], board_ai[2][4], board_ai[2][5], sep="")
        print("4", board_ai[3][0], board_ai[3][1], board_ai[3][2], board_ai[3][3], board_ai[3][4], board_ai[3][5], sep="")
        print("5", board_ai[4][0], board_ai[4][1], board_ai[4][2], board_ai[4][3], board_ai[4][4], board_ai[4][5], sep="")
        print("6", board_ai[5][0], board_ai[5][1], board_ai[5][2], board_ai[5][3], board_ai[5][4], board_ai[5][5], sep="")
        print("")

    #player:
        print("    ----Player1:-----\n")
        print(" ", " A", " B", " C", " D", " E", " F", sep="")
        print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
        print("2", board_player[1][0], board_player[1][1], board_player[1][2], board_player[1][3], board_player[1][4], board_player[1][5], sep="")
        print("3", board_player[2][0], board_player[2][1], board_player[2][2], board_player[2][3], board_player[2][4], board_player[2][5], sep="")
        print("4", board_player[3][0], board_player[3][1], board_player[3][2], board_player[3][3], board_player[3][4], board_player[3][5], sep="")
        print("5", board_player[4][0], board_player[4][1], board_player[4][2], board_player[4][3], board_player[4][4], board_player[4][5], sep="")
        print("6", board_player[5][0], board_player[5][1], board_player[5][2], board_player[5][3], board_player[5][4], board_player[5][5], sep="")
        print("")

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

def ai():
    global is_hit
    #global ai_hits
    print("Computer's turn")
    time.sleep(2)
    if is_hit == True:
        last_shot = ai_hits[-1] 
        x = last_shot[0]
        y = last_shot[1]
        if x+1 < len(board_player):
            board_player[x+1][y] = bl 
            ai_hits.append((x+1,y))
            # kéne check, hogy talált-e és hogy kell-e állitani az is_hit-et 
        else:
            board_ai[x-2][y] = bl
            ai_hits.append((x-2,y))
    else:
        shot = random.choice(allowed_position) 
        x = shot[0]
        y = shot[1] #az abc  
        print(y+1,x+1)  
        # abc = "abcdef"
        # 123 = 123456  
        # dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

        time.sleep(1)
        while shot in ai_hits:
            shot = random.choice(allowed_position) 
            print("....")
        if board_player[x][y] == gr:
            board_player[x][y] = re 
            is_hit = True 
            ai_hits.append(shot)
            print("Hit!")
            time.sleep(2)
        else:
            board_player[x][y] = bu 
            print("Miss...")
            time.sleep(2)
            ai_hits.append(shot)
        #print(is_hit)
        time.sleep(1)

def check_hit(user_input):
    y = 'abcdef'.index(user_input[0])
    x = '123456'.index(user_input[1])

    if board_ai_ships[x][y] == 0:
        board_ai[x][y] = bu
        print("Miss!")
    elif board_ai_ships[x][y] == 2:
        board_ai[x][y] = re
        print("Hit!!")  
        #pprint.pprint(board_ai)

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

    # print("    ----Player1:-----\n")
    # print(" ", " A", " B", " C", " D", " E", " F", sep="")
    # print("1", board_player[0][0], board_player[0][1], board_player[0][2], board_player[0][3], board_player[0][4], board_player[0][5], sep="")
    # print("2", board_player[1][0], board_player[1][1], board_player[1][2], board_player[1][3], board_player[1][4], board_player[1][5], sep="")
    # print("3", board_player[2][0], board_player[2][1], board_player[2][2], board_player[2][3], board_player[2][4], board_player[2][5], sep="")
    # print("4", board_player[3][0], board_player[3][1], board_player[3][2], board_player[3][3], board_player[3][4], board_player[3][5], sep="")
    # print("5", board_player[4][0], board_player[4][1], board_player[4][2], board_player[4][3], board_player[4][4], board_player[4][5], sep="")
    # print("6", board_player[5][0], board_player[5][1], board_player[5][2], board_player[5][3], board_player[5][4], board_player[5][5], sep="")
    # print("")

    #Player:        
    print ("Player 1: \n".center(len(maxlength2)))
    print('{0:>{width}}A {0:>{width}}B {0:>{width}}C {0:>{width}}D {0:>{width}}E {0:>{width}}F'.format(space, width=maxlength))
    for i in yy:
        print("".join(["1 ", board_player[0][0]*zz+"|", board_player[0][1]*zz+"|", board_player[0][2]*zz+"|", board_player[0][3]*zz+"|", board_player[0][4]*zz+"|", board_player[0][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
    for i in yy:
        print("".join(["2 ", board_player[1][0]*zz+"|", board_player[1][1]*zz+"|", board_player[1][2]*zz+"|", board_player[1][3]*zz+"|", board_player[1][4]*zz+"|", board_player[1][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
    for i in yy:
        print("".join(["3 ", board_player[2][0]*zz+"|", board_player[2][1]*zz+"|", board_player[2][2]*zz+"|", board_player[2][3]*zz+"|", board_player[2][4]*zz+"|", board_player[2][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
    for i in yy:
        print("".join(["4 ", board_player[3][0]*zz+"|", board_player[3][1]*zz+"|", board_player[3][2]*zz+"|", board_player[3][3]*zz+"|", board_player[3][4]*zz+"|", board_player[3][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))
    for i in yy:
        print("".join(["5 ", board_player[4][0]*zz+"|", board_player[4][1]*zz+"|", board_player[4][2]*zz+"|", board_player[4][3]*zz+"|", board_player[4][4]*zz+"|", board_player[4][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))                      
    for i in yy:
        print("".join(["6 ", board_player[5][0]*zz+"|", board_player[5][1]*zz+"|", board_player[5][2]*zz+"|", board_player[5][3]*zz+"|", board_player[5][4]*zz+"|", board_player[5][5]*zz+"|"]))
    print("".join(["  ", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-", "--"*zz+"-"]))   
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
    print_board_zoom()
    check_hit(player_input())
    time.sleep(1)
    os.system('clear')
    print_board_zoom()
    ai() 
    check_winning()