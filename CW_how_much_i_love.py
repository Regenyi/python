def how_much_i_love_you(nb_petals):
    poem = {1: "I love you", 2: "a little", 3: "a lot", 4: "passionately", 5: "madly", 6: "not at all"}
    poem_line = nb_petals % 6 
    return poem[poem_line]
    print(poem[poem_line])

how_much_i_love_you(3)
