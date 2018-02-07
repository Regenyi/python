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

allowed_chars = [(0,0), (0,1), "a3", "a4", "a5",
                 (1,0), "b2", "b3", "b4", "b5",
                 "c1", "c2", "c3", "c4", "c5",
                 "d1", "d2", "d3", "d4", "d5",
                 "e1", "e2", "e3", "e4", "e5",
                 "f1", "f2", "f3", "f4", "f5",
                 ]

elso_hajo = random.choice(allowed_chars)
#print(elso_hajo)
#place ship:
x = 'abcdef'.index(elso_hajo[0]) 
y = '123456'.index(elso_hajo[1])
board_ai[x][y] = 2 #black

if x+2 > len(board_ai) 
    aaaa
elif: 
    x-2 < 0

allowed_chars.remove(elso_hajo)
allowed_chars.remove((x-2,0))




    board_ai[x+1][y] = 2 # if x+1 is out of range try x-1 (másiknál majd Y), lehet hogy safe zone miatt csak b2-tőle4-ig legyen a random pool?


board_ai[x+2][y] = 2 # if x+2 is out of range try x-1, vagy x-2 


pprint.pprint(board_ai)

masodik_hajo = random.choice(allowed_chars)

