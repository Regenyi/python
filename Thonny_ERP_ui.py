def print_table(table, title_list):
    full_table = table
    full_table.insert(0, title_list) # insert title id-s into table

    coloumns_length = []  # width is better 
    for k in title_list:  # count titles length and saves it in columns_lenght list
        a = len(k) 
        coloumns_length.append(a) 

    n = 0 
    for i in range(len(table[0])): 
        # print("Coloumn {}".format(i + 1))
        for j in table:  # j = row, n = coloumn
            # print(j[n])
            if coloumns_length[i] < len(str(j[n])):  # + convert to string in order to have length
                coloumns_length[i] = len(str(j[n]))
        n += 1

    # top_line = "┏"
    # for i in range(len(title_list)):
    #     if i < len(title_list)-1:
    #         top_line += "{:━^{width}}{}".format("", "┳", width=(i))
    #     else:
    #         top_line += "{:━^{width}}{}".format("", "━", width=(i)-1)
    # top_line += "┓"

    for i in full_table:  # print the table in the "correct" look
        print("━" * ((total(coloumns_length) + (len(coloumns_length) * 3) + 1)))
        # print("")
        c = 0
        for j in i:
            print('{} {:^{width}}'.format("┃", i[c],  width=coloumns_length[c]), end=" ")
            c += 1
        print("┃")
    print("━" * ((total(coloumns_length) + (len(coloumns_length) * 3) + 1)))

    full_table.pop(0)

def total(lista):
    tot = 0
    for i in range(len(lista)):
        tot = tot + lista[i]
    return tot

table4 = [['kH34Ju#&', 'PlayStation 4', 'Sony', '2013', '4'], ['jH34Ju#&', 'Xbox One', 'Microsoft', '2013', '4'], ['tH34Ju#&', 'Wii Next generation', 'Nintendo', '2012', '3'], ['eH34Ju#&', 'Nintendo 3DS', 'Nintendo', '2011', '2'], ['bH34Ju#&', 'PlayStation Vita', 'Sony', '2011', '4'], ['vH34Ju#&', 'Wii', 'Nintendo', '2006', '5'], ['kH14Ju#&', 'PlayStation 3', 'Sony', '2006', '4'], ['kH35Ju#&', 'Xbox 360', 'Microsoft', '2005', '4'], ['kH38Ju#&', 'Nintendo DS', 'Nintendo', '2004', '3'], ['kH94Ju#&', 'PlayStation Portable', 'Sony', '2004','2']]
title_list = ['ID', 'Name', 'Manufacturer', 'Purchase_date', 'Durability']
print_table(table4, title_list)