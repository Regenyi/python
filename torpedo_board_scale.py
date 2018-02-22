import pprint

abc = ["a","b","c","d","e","f","g","h","i","j"]
num = ["1","2","3","4","5","6","7","8","9"]

allowed_chars2 = []
változó = 5

# for i in abc[:változó]:
#     for j in num[:változó]:
#         allowed_chars2.append(i+j)

allowed_chars2 = [i+j for i in abc[:változó] for j in num[:változó]]



def print_board():
    #ai:
        print("   Computer:\n")
        print(" ", " A", " B", " C", " D", " E", " F", sep="")
        print("1", board_ai[0][0], board_ai[0][1], board_ai[0][2], board_ai[0][3], board_ai[0][4], board_ai[0][5], sep="")
        print("2", board_ai[1][0], board_ai[1][1], board_ai[1][2], board_ai[1][3], board_ai[1][4], board_ai[1][5], sep="")
        print("3", board_ai[2][0], board_ai[2][1], board_ai[2][2], board_ai[2][3], board_ai[2][4], board_ai[2][5], sep="")
        print("4", board_ai[3][0], board_ai[3][1], board_ai[3][2], board_ai[3][3], board_ai[3][4], board_ai[3][5], sep="")
        print("5", board_ai[4][0], board_ai[4][1], board_ai[4][2], board_ai[4][3], board_ai[4][4], board_ai[4][5], sep="")
        print("6", board_ai[5][0], board_ai[5][1], board_ai[5][2], board_ai[5][3], board_ai[5][4], board_ai[5][5], sep="")
        print("")

board_ai = []
allowed_position = [("board_ai",[x],[y]) for x in range(6) for y in range(6)]

allowed_position = [(x, y) for x in range(6) for y in range(6)]
print(allowed_position)

BL = ("\033[0;37;41m  \033[0m")

board_ai = [
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
]

pprint.pprint(board_ai)