def score(game):
    game = game.lower()
    result = 0
    frame = 1 # a game of bowling consists of 10 frames
    in_first_half = True
    for i in range(len(game)):   
        if game[i] == '/':
            result += 10 - last
        else:
            result += roll(game[i])
        if frame < 10  and roll(game[i]) == 10:  # 10-es guritásnál 10 dobás alatt
            if game[i] == '/': 
                result += roll(game[i+1])
            elif game[i] == 'x':    # ha strike akkor 
                result += roll(game[i+1])  
                if game[i+2] == '/': # ha a köv dobás / akkor 10-dobás plusz pont
                    result += 10 - roll(game[i+1]) 
                else:
                    result += roll(game[i+2]) # ha nem, akkor 
        last = roll(game[i])
        if not in_first_half: 
            frame += 1
        in_first_half = not in_first_half # a bowler has two chances per frame to knock down all ten pins block
        if game[i] == 'x':
            in_first_half = True
            frame += 1
    return result

def roll(char):   
    if char in '123456789':
        return int(char)
    elif char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

score("5/3-----------------")