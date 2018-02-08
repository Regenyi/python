# Globals:
re = ("\033[0;37;41m  \033[0m")
bl = ("\033[0;37;40m  \033[0m")
title = [" ", "A", "B", "C", "D", "E", "F"]
A = "a"
B = "a"
C = "a"
winning = False

board_ai = [
    [bl, bl, bl, bl, bl, bl],
    [re, re, re, re, re, re],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
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

print(winning)

def check_winning():
    global winning  
    if (sum(row.count(re) for row in board_ai)) > 1:
        print("the winner is: player 1")
        print("")
        winning = True 
        
    elif (sum(row.count(re) for row in board_player)) >= 16:
        print("the winner is: the computer")
        print("")
        winning = True 
    else:
        pass
    
check_winning()
print(winning)
