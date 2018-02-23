abc = ["a","b","c","d","e","f","g","h","i","j"]
num = ["1","2","3","4","5","6","7","8","9"]

allowed_chars2 = []
változó = 5

# ilyen volt: 
allowed_chars = ("a1", "a2", "a3", "a4", "a5", "a6",
                 "b1", "b2", "b3", "b4", "b5", "b6",
                 "c1", "c2", "c3", "c4", "c5", "c6",
                 "d1", "d2", "d3", "d4", "d5", "d6",
                 "e1", "e2", "e3", "e4", "e5", "e6",
                 "f1", "f2", "f3", "f4", "f5", "f6",
                 )

# ilyen lett: 
allowed_chars2 = [i+j for i in abc[:változó] for j in num[:változó]]

# ilyen volt: 
board_player = [
    [RE, GR, BL, BL, BL, BL],
    [BL, RE, BL, BL, BL, BL],
    [BL, GR, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
    [BL, BL, BL, BL, BL, BL],
]

# ilyen lett: 
board_player = [[BL for x in range(6)] for y in range(6)]

# ilyen volt a loading és a save: 
célfájl = open('szoveg.txt', 'w')
for elem in board_ai:
    print(elem, file=célfájl)
for k,v in game_param.items():
    print(k, v, file=célfájl)
célfájl.close()

readfile = open('szoveg.txt', 'r')
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

# ilyen lett: 
def load_game():
    with open('torpedo.sav', 'rb') as f: 
        global game_param, board_player, board_ai, board_ai_ships, hits, player_hit, ai_hits
        game_param, board_player, board_ai, board_ai_ships, hits, player_hit, ai_hits = pickle.load(f)
    time.sleep(0.1)

def save_game():
    with open('torpedo.sav', 'wb') as f:  
        pickle.dump([game_param, board_player, board_ai, board_ai_ships, hits, player_hit, ai_hits], f)
    print("saved!")


# ilyen volt a globals:
re = ("\033[0;37;41m  \033[0m")
bl = ("\033[0;37;40m  \033[0m")
gr = ("\033[0;37;42m  \033[0m") 
bu = ("\033[0;37;44m  \033[0m")
winning = False
is_hit = False  
hits = []
player_hit = []
ai_hits = [(1, 1)]

# ilyen lett: 
game_param = {
    "winning": False,
    "gen": True, 
    "maxlength": 1.8,
    "score": 0,
    "game_over": False,
    "high_score": 0,
    "size": 0
    }

print("score:", game_param["score"])