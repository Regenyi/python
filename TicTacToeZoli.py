import re 

board=[1,"X",3,4,5,6,7,8,9]
winning = False
player1 = False

def print_board():
    print(board[0], "|" ,board[1], "|" ,board[2], "|")
    print("––––––––––––")
    print(board[3], "|" ,board[4], "|" ,board[5], "|")
    print("––––––––––––")
    print(board[6], "|" ,board[7], "|" ,board[8], "|")
    print("")
print_board() 

while winning == False:  
#def user_input():
    player1_input = input("Press available number on numkeys:\n")
    # while True:
    #     if len(player1_input) > 1: 
    #         print("wrong format!")
    #         player1_input = input("Press available number on numkeys:\n") 
    #     elif re.search("[a-z]",player1_input):
    #         print("wrong format!")
    #         player1_input = input("Press available number on numkeys:\n") 
    #     else:
    #         break 
        
    player1_input = int(player1_input)
    #player1_input = input("Press available number on numkeys:\n")
    if board[player1_input] != "X" and board[player1_input] != "O":
        board[player1_input] = 'X'

    # for i in range(1,10):
    #     if player1_input == i:
    #         if board[i-1]=="X":
    #             print("a")
    #             print("Wrong format!")
    #             player1_input = input("Press available number on numkeys:\n")

        else: 
            for i in range(1,10):
                if player1_input == i:
                    board[i-1]="X"
                    player1 = True
    
    print_board()
    print(board)

	# else player == player2:
	# 	print("player2")
	# 	player = player1

    print(winning)


    # player2_input = int(input("Press available number on numkeys:\n"))
    # print("player2")
    # # while True:
    #     if len(player1_input) > 1: 
    #         print("wrong format!")
    #         player1_input = int(input("Press available number on numkeys:\n")) 
    #     elif re.search("[a-z]",player1input):
    #         print("wrong format!")
    #         player1_input = int(input("Press available number on numkeys:\n")) 
    #     else:
    #         break 
    # for i in range(1,10):
    #     if player2_input == i:
    #         board[i-1]="o"

    #user_input()
    # print_board()
    # print(board)
    # print(winning)


    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or \
       (board[0] == "X" and board[1] == "X" and board[2] == "X"):
        winning = True 
        print("winner is")
        break


print_board()




