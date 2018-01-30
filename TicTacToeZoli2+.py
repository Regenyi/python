import re 
import os
import random
import time
import signal 
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl-C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

winning = False
board=[1,2,3,4,5,6,7,8,9]
os.system("clear")

def print_board():
    print(board[0], "|" ,board[1], "|" ,board[2], "|")
    print("––––––––––––")
    print(board[3], "|" ,board[4], "|" ,board[5], "|")
    print("––––––––––––")
    print(board[6], "|" ,board[7], "|" ,board[8], "|")
    print("")

while True:
    #two_player = input("2 player or computer"?)
    #if two_player == 1: 

    while winning == False: 
        # player 1
        os.system("clear")  
        print_board() 
        player_input = input("Press available number on numkeys:\n")
        if player_input == "e" :
             exit() 
        while True:
            if not re.search("[0-9]",player_input) or player_input == "exit":
                print("wrong format!")
                player_input = input("Press available number on numkeys:\n") 
            else:
                break  
        player_input = int(player_input)

        while True:
            if board[player_input] == "X" or board[player_input] == "O":
                player_input = int(input("Taken, Press available number on numkeys:\n")) 
                os.system("clear")
                print_board()
            else:
                board[player_input] = 'X'
                break 

        if (board[0] == "X" and board[1] == "X" and board[2] == "X") or \
        (board[0] == "X" and board[1] == "X" and board[2] == "X"):
            winning = True 
            print("winner is")
            break
        
        os.system("clear")
        print_board()

        player_input = input("Press available number on numkeys player2:\n")
        while True:
            if not re.search("[0-9]",player_input):
                print("wrong format!")
                player_input = input("Press available number on numkeys p2:\n") 
            else:
                break   
        player_input = int(player_input)

        if board[player_input] == "X" or board[player_input] == "O":
            print("Taken")
            print("")
            time.sleep(1)
        else:
            board[player_input] = 'O'
            print_board()
            print(board)

        if (board[0] == "O" and board[1] == "O" and board[2] == "O") or \
        (board[0] == "X" and board[1] == "X" and board[2] == "X"):
            winning = True 
            print("winner is")
            break

        os.system("clear")
        print_board()

    #if two_player == 2:
    #   copy  

    cont = input("Press Y to play again!") 
    if cont != "y":
        break
    else:
        winning = False
        board=[1,2,3,4,5,6,7,8,9] 







