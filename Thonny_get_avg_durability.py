def get_average_durability_by_manufacturers(table):

    count_games = {}

    for i in range(len(table)):
        if table[i][2] not in count_games:
            count_games[table[i][2]] = 1
        else:
            count_games[table[i][2]] += 1

    game_durability = {}

    for i in range(len(table)):
        if table[i][2] not in game_durability.keys():
            game_durability[table[i][2]] = int(table[i][4])
        else:
            game_durability[table[i][2]] += int(table[i][4])

    game_final = {}

    for manufacturer in game_durability.keys():
        average_number = game_durability[manufacturer]/count_games[manufacturer]
        game_final[manufacturer] = average_number

    title_list = ['Manufacturer', 'Average durability']

    game = []

    for i, j in game_final.items():
        game.append([i, j])
    os.system("clear")
    ui.print_table(game, title_list)


table4 = [['kH34Ju#&', 'PlayStation 4', 'Sony', '2013', '4'], ['jH34Ju#&', 'Xbox One', 'Microsoft', '2013', '4'], ['tH34Ju#&', 'Wii Next generation', 'Nintendo', '2012', '3'], ['eH34Ju#&', 'Nintendo 3DS', 'Nintendo', '2011', '2'], ['bH34Ju#&', 'PlayStation Vita', 'Sony', '2011', '4'], ['vH34Ju#&', 'Wii', 'Nintendo', '2006', '5'], ['kH14Ju#&', 'PlayStation 3', 'Sony', '2006', '4'], ['kH35Ju#&', 'Xbox 360', 'Microsoft', '2005', '4'], ['kH38Ju#&', 'Nintendo DS', 'Nintendo', '2004', '3'], ['kH94Ju#&', 'PlayStation Portable', 'Sony', '2004','2']]
get_average_durability_by_manufacturers(table4)
