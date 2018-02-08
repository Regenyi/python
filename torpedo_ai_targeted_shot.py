import random

board_ai = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

allowed_chars = ["a1", "a2", "a3", "a4", "a5",
                 "b1", "b2", "b3", "b4", "b5",
                 "c1", "c2", "c3", "c4", "c5",
                 "d1", "d2", "d3", "d4", "d5",
                 "e1", "e2", "e3", "e4", "e5",
                 "f1", "f2", "f3", "f4", "f5",
                 ]

elso_hajo = random.choice(allowed_chars)
print(elso_hajo)

#place ship:
x = 'abcdef'.index(elso_hajo[0])
y = '123456'.index(elso_hajo[1])
board_ai[x][y] = 2 #black 
board_ai[x+1][y] = 2 #black 

allowed_chars.remove(elso_hajo)
allowed_chars.remove() 

print(board_ai)

masodik_hajo = random.choice(allowed_chars)
is_hit = True  
ai_hits = []

if is_hit == True:
    shot = last shot + - 
    x = elso_hajo[0]
    y = elso_hajo[1]
    board_ai[x][y] = 2  

    if x+2 < len(board_ai):
        board_ai[x+2][y] = 2
        board_ai[x+1][y] = 2
        # allowed_chars.remove((x+1,y))
        # allowed_chars.remove((x+2,y))
    else:
        board_ai[x-2][y] = 2
        board_ai[x-1][y] = 2

else:
    shot = random.choice(allowed_chars) 
    if shot in ai_hits:
        print("....")
    elif shot in board_player == "Hajó":
        board_player[x][y] = 2 
        is_hit = True 
        hits.append(ai_hits)
    else:
        board_player[x][y] = 1 
        hits.append(ai_hits)






