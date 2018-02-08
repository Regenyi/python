import random
import pprint

board_ai = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# allowed_chars = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
#                  (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
#                  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
#                  (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
#                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
#                  (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
#                  ]


def position_gen():
    allowed_chars = [(x, y) for x in range(6) for y in range(6)]
    board_ai = [[0 for x in range(6)] for y in range(6)]

    elso_hajo = random.choice(allowed_chars)
    print(elso_hajo)
    # place ship:
    x = elso_hajo[0]
    y = elso_hajo[1]
    board_ai[x][y] = 2  

    if x+2 < len(board_ai):
        board_ai[x+2][y] = 2
        board_ai[x+1][y] = 2
        allowed_chars.remove((x+1,y))
        allowed_chars.remove((x+2,y))
    else:
        board_ai[x-2][y] = 2
        board_ai[x-1][y] = 2
        allowed_chars.remove((x-1,y))
        allowed_chars.remove((x-2,y))
        
    allowed_chars.remove(elso_hajo)

    # print(allowed_chars)
    # print("")

    masodik_hajo = random.choice(allowed_chars)
    print(masodik_hajo)
    x = masodik_hajo[0]
    y = masodik_hajo[1]
    board_ai[x][y] = 2  

    if y+1 < len(board_ai):
        board_ai[x][y+1] = 2
        #allowed_chars.remove((x,y+1))
    else:
        board_ai[x][y-1] = 2
        #allowed_chars.remove((x,y-1))
    
    pprint.pprint(board_ai)

while True:
    position_gen()
    start_choice = input("Press '1' to start with this board or press '2' to generate a new layout")
    if start_choice == "1":
        break        
    else:
        position_gen()  

position_gen()
print("break") 