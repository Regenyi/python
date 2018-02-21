import pickle

BL = 2

game_param = {
    "winning": 0,
    "gen": 1, 
    "maxlength": 2,
    "score": 0,
    "game_over": 0,
    "high_score": 0,
    "size": 0
    }

board_ai = [
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
]

print(board_ai)

célfájl = open('szoveg.txt', 'w')
for elem in board_ai:
    print(elem, file=célfájl)
for k,v in game_param.items():
    print(k, v, file=célfájl)
célfájl.close()

readfile = open('szoveg.txt', 'r')
#for elem in readfile:
n = 1
del board_ai[:]
while n <= 6:
    sor = readfile.readline().strip()
    board_ai.append((sor))
    n += 1
n = 1
while n <= 6:       
    for line in readfile:
        splitLine = line.split()
        game_param[(splitLine[0])] = int(splitLine[1])
    n += 1

readfile.close()

print(board_ai)
print(game_param)


# userinput = input("press 1 to save, or 2 to load: ")

# if userinput == "1":
#     with open('torpedo.sav', 'wb') as f:  
#         pickle.dump([game_param, board_ai], f)

# if userinput == "2":
#     # Getting back the objects:
#     with open('torpedo.sav', 'rb') as f: 
#         game_param, board_ai = pickle.load(f)

# print(game_param)


