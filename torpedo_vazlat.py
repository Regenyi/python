import time
import os

# Globals:
red = ("\033[0;37;41m  \033[0m") 
black = ("\033[0;37;40mXXX|\033[0m")
# maradék jelek: találat, mellé, hajó1, hajó2, aihajó1, aihajó2
player1 = 1
ai = 1
user_input = ""
winning = False

#######################
#    Board dolgok     #
#######################

board = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")
board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")
board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")
board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")
board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")
board[0][0] = board[0][1] = board[0][2] = board[0][3] = board[0][4] = board[0][5] = ("\033[0;37;41m   |\033[0m")

# kettő kell? a tied és a számgép és a számgép kirajzolása 
# Low prio: Hogy lehet felnagyitani a boardot x*y-ra, úgy hogy az escape karakterek megmaradjanak? :

def print_board(player, ai):
    if ai == ai:
        print("    ----Computer:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print(" ", board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], sep="")
        print("1", board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], sep="")
        print("")

    if player == player1:
        print("    ----Player1:-----\n")
        print(" ", " A ", "  B ", "  C ", "  D ", "  E ", "  F ", sep="")
        print(" ", board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], sep="")
        print("1", board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], sep="")
        # print(" ", row2[0],row2[1],row2[2],row2[3],row2[4],row2[5], sep="")
        # print("2", row2[0],row2[1],row2[2],row2[3],row2[4],row2[5], sep="")
        # print(" ", row3[0],row3[1],row3[2],row3[3],row3[4],row3[5], sep="")
        # print("3", row3[0],row3[1],row3[2],row3[3],row3[4],row3[5], sep="")
        # print(" ", row4[0],row4[1],row4[2],row4[3],row4[4],row4[5], sep="")
        # print("4", row4[0],row4[1],row4[2],row4[3],row4[4],row4[5], sep="")
        # print(" ", row5[0],row5[1],row5[2],row5[3],row5[4],row5[5], sep="")
        # print("5", row5[0],row5[1],row5[2],row5[3],row5[4],row5[5], sep="")
        # print(" ", row6[0],row6[1],row6[2],row6[3],row6[4],row6[5], sep="")
        # print("6", row6[0],row6[1],row6[2],row6[3],row6[4],row6[5], sep="")
        print("")

def position_gen():
    # a hajóknak szinkódja lenne 
    # addig generáltathat a player, amig nem tetszik neki az a leosztás 
    # szabály: a boardnál eggyel kissebb sávban 2 db álló hajó egy 2-s egy 3-as, ami nem lehet egymáson 
    # ha oké, akkor az ainak is legenerálódik a sajátja csak fekvőben 
    pass

def player_input():
    #while True user_input != "a1": # allowed_chars / lőtt-e már oda, ez legyen egy külön appendelt lista?
    user_input = input("Hova lősz?")
    return user_input

def check_winning():
    # összehasonlitása a két táblának (truth table)
    # winning = True 
    # print("the winner is {}".format(winner)"
    pass

def check_hit():
    # ennek a függvénynek kell bemenet, hogy melyik playert nézze és annak a playernek az inputja
    # és kell az a tábla, amivel összeveti a találatot és hogy odamár lőttek-e
    # ha már lőtt, akkor vissza kellene lépnie a player_input-ra vagy az ai-ra, hogy lőjjön újat 
    if user_input == "A1" or "a1":
        board[0][0] = black
    elif user_input == "B1" or "b1":
        board[0][0] = black
    else:
        pass

def ai():
    # when to call?
    # with what input, output should be a shot on the board
    # random shot ha nincs találat ág
    # ha találat ág van, akkor a találathoz képest +/-1 cella és +-/1 row-la löjje a következő lépéseit 
    pass

while winning == False:
    # logika jó e igy? mit kell minek átadnia hogy jó legyen?
    os.system('clear')
    position_gen() 
    print_board(player1, ai)
    player_input()
    check_hit()
    time.sleep(1)
    ai()
    check_winning()