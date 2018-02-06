import time 
import os
row1=[1,2,3,4,5,6]
row2=[1,2,3,4,5,6]
i = range(1,7) 

red = ("\033[0;37;41m \033[0m")

row1[0] = red
#row1[0] = ("\033[0;37;41m \033[0m")
row2[0] = ("\033[1;31;40m \033[0m")



player1 = 1 

def print_board(player):
    if player == player1:
        print(" ", "A","B","C","D","E", sep="")
        print("1", row1[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="") 
        print("2", row2[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="")
        print("3", row2[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="")
        print("4", row2[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="")
        print("5", row2[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="")
        print("6", row2[0],row1[1],row1[2],row1[3],row1[4],row1[5], sep="")

def position_gen(player):
    pass

def user_input(char):

    pass

def check_winning():
    pass

def check_hit():
    pass

def ai():
    # when to call?
    # with what input , output should be a shot on the board 
    pass

os.system('clear')
print_board(player1)

user_input = ()
while user_input != "a1": # allowed_chars valid chars instead a1 
    try:
        user_input=input("target?")
    except ValueError:
        print("wrong format")

    if user_input == "A1" or "a1":
        row1[0] = ("\033[1;32;40mX\033[0m")

os.system('clear')
print_board(player1)   






