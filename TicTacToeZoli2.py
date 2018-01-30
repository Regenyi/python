import re 
import os
import random

winning = False
os.system("clear")
board=[1,2,3,4,5,6,7,8,9]


def print_board():
    print(board[0], "|" ,board[1], "|" ,board[2], "|")
    print("––––––––––––")
    print(board[3], "|" ,board[4], "|" ,board[5], "|")
    print("––––––––––––")
    print(board[6], "|" ,board[7], "|" ,board[8], "|")
    print("")

def computer():
     random.seed
     move = random.randrange(1,9)
     board[move] = 'o'
    

print_board()

while winning == False:  
    player_input = input("Press available number on numkeys:\n")
    while True:
        if len(player_input) > 1: 
            print("wrong format!")
            player_input = input("Press available number on numkeys:\n") 
        elif re.search("[a-z]",player_input):
            print("wrong format!")
            player_input = input("Press available number on numkeys:\n") 
        else:
            break   
    player_input = int(player_input)

    if board[player_input-1] == "X" or board[player_input-1] == "O":
        print("Taken") 
        print("")
    else:
        board[player_input-1] = 'X'
        print(board)

    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or \
       (board[0] == "X" and board[1] == "X" and board[2] == "X"):
        winning = True 
        print("winner is")
        break
    
    os.system("clear")
    print_board()

    computer()

    # player_input = input("Press available number on numkeys player2:\n")
    # while True:
    #     if len(player_input) > 1: 
    #         print("wrong format!")
    #         player_input = input("Press available number on numkeys p2:\n") 
    #     elif re.search("[a-z]",player_input):
    #         print("wrong format!")
    #         player_input = input("Press available number on numkeys p2:\n") 
    #     else:
    #         break   
    # player_input = int(player_input)

    if board[player_input-1] == "X" or board[player_input-1] == "O":
        print("Taken")
        print("")
    else:
        board[player_input-1] = 'O'
        print_board()
        print(board)

    if (board[0] == "O" and board[1] == "O" and board[2] == "O") or \
       (board[0] == "X" and board[1] == "X" and board[2] == "X"):
         winning = True 
         print("winner is")
         break
    
    
    os.system("clear")
    print_board()




