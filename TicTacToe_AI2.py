# TTT by KZ, RA for CC Python TW1 
# todo: expand exception handler to taken, fix taken loop slip with ai 

import re 
import os
import random
import time

# Init:
winning = False
os.system("clear")
board=[1,2,3,4,5,6,7,8,9]
print("Instructions: \n\n Play with the numpad, press CTRL-C to exit.\n")
time.sleep(5) 

# Printing the board func:
def print_board():
    print(board[0], "|" ,board[1], "|" ,board[2], "|")
    print("––––––––––––")
    print(board[3], "|" ,board[4], "|" ,board[5], "|")
    print("––––––––––––")
    print(board[6], "|" ,board[7], "|" ,board[8], "|")
    print("")

# Check who is the winner custom func:
def winner(board,player): 
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        return True 
    else: 
        return False     

# Main loop:
while True: 
    os.system("clear")
    player = input("Type '1' for one player vs Computer \n  or '2' for two players: ")
    if player == str("exit"):
        exit()
    
    # One player mode:
    if player == "1": 
        os.system("clear")
        print_board()
        while winning == False:

            # Human player: 
            player_input = input("Press available number on numkeys:\n")

            # Exception handling:
            while True: 
                if len(player_input) > 1: 
                    os.system("clear")
                    print_board()
                    print("wrong format!")
                    player_input = input("Press available number on numkeys:\n") 
                elif re.search("[a-z]",player_input):
                    os.system("clear")
                    print_board() 
                    print("wrong format!")
                    player_input = input("Press available number on numkeys:\n")
                else:
                    break  

            # Check for taken cell:
            player_input = int(player_input)
            while True:
                if board[player_input-1] == "X" or board[player_input-1] == "\033[1;32;40mo\033[0m":
                    os.system("clear")
                    print_board()
                    player_input = int(input("Already taken! Press available number on numkeys:\n")) 
                else:
                    board[player_input-1] = 'X'
                    break 

            # X checks for winner:
            if winner(board,"X"):
                os.system("clear")
                print("\nWinner is X!")
                time.sleep(2)
                break

            # Literal winner table:
                # if (board[0] == "o" and board[1] == "o" and board[2] == "o") or \
                #     (board[3] == "o" and board[4] == "o" and board[5] == "o") or \
                #     (board[6] == "o" and board[7] == "o" and board[8] == "o") or \
                #     (board[0] == "o" and board[3] == "o" and board[6] == "o") or \
                #     (board[1] == "o" and board[4] == "o" and board[7] == "o") or \
                #     (board[2] == "o" and board[5] == "o" and board[8] == "o") or \
                #     (board[0] == "o" and board[4] == "o" and board[8] == "o") or \
                #     (board[2] == "o" and board[4] == "o" and board[6] == "o"):
                #   winning = True 
                #   print("winner is")
                #   break         
                          
            # X checks for tie:
            elif board.count("X") == 5 and board.count("\033[1;32;40mo\033[0m") == 4 or \
                board.count("X") == 4 and board.count("\033[1;32;40mo\033[0m") == 5:
                winning = True
                os.system("clear")
                print("\nIt's a tie!")
                time.sleep(2)
                break

            # "AI"
            move = random.randrange(1,9,_int=int)

            # Check columns     
            for i in [0,1,2]:
                if board[i] == "X" and board[i+3] == "X" and board[i+6] == 7: 
                    board[i+6] = ("\033[1;32;40mo\033[0m")
                if board[i] == "X" and board[i+3] == 4 and board[i+6] == "X": 
                    board[i+3] = ("\033[1;32;40mo\033[0m")
                if board[i] == 1 and board[i+3] == "X" and board[i+6] == "X": 
                    board[i] = ("\033[1;32;40mo\033[0m")

            # Checks if the middle cell is empty: 
            while True:
                if board[4]==5:
                    board[4] = ("\033[1;32;40mo\033[0m")
                    os.system("clear")
                    print_board()
                    break
                    
                elif board[move] == "X" or board[move] == "\033[1;32;40mo\033[0m":
                    move = random.randrange(1,9,_int=int)
                    print("Thinking")  

                else:
                    board[move] = ("\033[1;32;40mo\033[0m")
                    os.system("clear")
                    print_board()
                    break 

            # Checks for tie: 
            if board.count("X") == 5 and board.count("\033[1;32;40mo\033[0m") == 4 or \
                board.count("X") == 4 and board.count("\033[1;32;40mo\033[0m") == 5:
                    winning = True
                    os.system("clear")
                    print("\nIt's a tie!")
                    time.sleep(2)
                    break 

            # Ai checks for winner:
            if winner(board,"\033[1;32;40mo\033[0m"):
                os.system("clear")
                print("\nWinner is O!")
                time.sleep(2)
                break
                
        # New game:
        os.system("clear")
        cont = input("Do you want to play again? (Y/N) \n")
        if cont != str("y"):
            break
        else:
            winning = False 
            board=[1,2,3,4,5,6,7,8,9] 
            os.system("clear")

    ##################
    # Two player mode:
    ##################

    if player == "2": 
        os.system("clear")
        print_board()
        while winning == False:

            # Player X: 
            player_input = input("Press available number on numkeys Player 1:\n")

            # Exception handling:
            while True: 
                if len(player_input) > 1: 
                    os.system("clear")
                    print_board()
                    print("wrong format!")
                    player_input = input("Press available number on numkeys Player 1:\n") 
                elif re.search("[a-z]",player_input):
                    os.system("clear")
                    print_board() 
                    print("wrong format!")
                    player_input = input("Press available number on numkeys Player 1:\n")
                else:
                    break  

            # Check for taken cell:
            player_input = int(player_input)
            while True:
                if board[player_input-1] == "X" or board[player_input-1] == "\033[1;32;40mo\033[0m":
                    os.system("clear")
                    print_board()
                    player_input = int(input("Already taken, press available number on numkeys Player 1:\n")) 
                else:
                    board[player_input-1] = 'X'
                    break 

            # X checks for winner:
            if winner(board,"X"):
                os.system("clear")
                print("\nWinner is X!")
                time.sleep(2)
                break

            # X checks for tie:
            elif board.count("X") == 5 and board.count("\033[1;32;40mo\033[0m") == 4:
                winning = True
                os.system("clear")
                print("\nIt's a tie!")
                time.sleep(2)
                break

            os.system("clear")
            print_board()

            # Player O:
            player_input = input("Player 2, press available number on numkeys:\n")

            # Exception handling:
            while True: 
                if len(player_input) > 1: 
                    os.system("clear")
                    print_board()
                    print("wrong format!")
                    player_input = input("Player 2, press available number on numkeys X:\n") 
                elif re.search("[a-z]",player_input):
                    os.system("clear")
                    print_board() 
                    print("wrong format!")
                    player_input = input("Player 2, press available number on numkeys:\n")
                else:
                    break  

            # Check for taken cell:
            player_input = int(player_input)
            while True:
                if board[player_input-1] == "X" or board[player_input-1] == "\033[1;32;40mo\033[0m":
                    os.system("clear")
                    print_board()
                    player_input = int(input("Already taken! Press available number on numkeys Player 2:\n")) 
                else:
                    board[player_input-1] = "\033[1;32;40mo\033[0m"
                    break 

            # O checks for winner:
            if winner(board,"\033[1;32;40mo\033[0m"):
                os.system("clear")
                print("\nWinner is O!")
                time.sleep(2)
                break

            # O checks for tie:
            elif board.count("X") == 5 and board.count("\033[1;32;40mo\033[0m") == 4:
                winning = True
                os.system("clear")
                print("\nIt's a tie!")
                time.sleep(2)
                break

            os.system("clear")
            print_board()

        # New game:
        os.system("clear")
        cont = input("Do you want to play again? (Y/N) \n")
        if cont != str("y"):
            break
        else:
            winning = False 
            board=[1,2,3,4,5,6,7,8,9] 
            os.system("clear")
      