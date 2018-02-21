import pickle

BL = 2

game_param = {
    "winning": False,
    "gen": True, 
    "maxlength": 2.8,
    "score": 0,
    "game_over": False,
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

print(game_param)
userinput = input("press 1 to save, or 2 to load: ")

if userinput == "1":
    with open('torpedo.sav', 'wb') as f:  
        pickle.dump([game_param, board_ai], f)

if userinput == "2":
    # Getting back the objects:
    with open('torpedo.sav', 'rb') as f: 
        game_param, board_ai = pickle.load(f)

print(game_param)

