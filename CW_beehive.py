def how_many_bees3(hive): # Norbis 
    if hive:
        bees_list = []
        for x in range(len(hive[0])):
            bees_list.append("".join(row[x] for row in hive)) # !!!!!!
        summa = 0
        for i in hive:
            i2 = "".join(i)
            summa = summa + i2.count("bee") + i2.count("eeb")
        summa2 = 0
        for i in bees_list:
            i3 = "".join(i)
            summa2 = summa2 + i3.count("bee") + i3.count("eeb")             
        print(summa+summa2)
        return summa+summa2
    return 0


def how_many_bees2(hive):
    if hive == None:
        return None
    else:
        b = "bee"
        bees_list = []
        x = 0
        for n in range(7): 
            bees_list.append("".join(hive[0][x]+hive[1][x]+hive[2][x]))
            x += 1
        summa = 0
        for i in hive:
            i2 = "".join(i)
            summa = summa + i2.count("bee")   
        summa2 = 0
        for i in hive:
            i2 = "".join(i)
            summa2 = summa2 + i2.count(b[::-1]) 
        summa3 = bees_list.count("bee") + bees_list.count("eeb")
        return summa+summa2+summa3

def how_many_bees(hive):
    b = "bee"
    bees_list = []
    x = 0
    for n in range(7): 
        bees_list.append("".join(hive[0][x]+hive[1][x]+hive[2][x]))
        x += 1
    summa = 0
    for i in hive:
        summa = summa + i.count(b)      
    summa2 = 0
    for i in hive:
        summa2 = summa2 + i.count(b[::-1]) 
    summa = summa + summa2 + bees_list.count("bee") + bees_list.count("eeb")
    print(summa)

hive2 = ["bee.bee",
        "e.e.e.e",
        "eeb.eeb"]

hive = ["bez",
        "xbd"]

hive3 = ["b..beeeee.b.ee.e.b",
        "ebbe.e.be.e.eb.e.e",
        "eee.eb.beee...ebb.",
        ".eee..eeb..ebb.bee",
        "bb.eee.eeeebb...e.",
        "...eeeeb.e.e.ebbeb",
        ".eee.ee.eebe..bb.b",
        "..eeebb.e.ebeb..ee",
        "ebee.ebeee.e..b.b.",
        "e.e.beee...ee.bbbe",
        "ebebee.eb.e..ee..b",
        ".bbe.bb..eeee.e.ee",
        "eeeee..eb.b.be..eb",
        "eb.eb..eee...ebeeb",
        ".ee.bee..bbbee.e.e",
        "eee.bebee..e.eb..b",
        ".ee.e..eebbbb.e.ee",
        "...ebbee.eee.beb.e"]
# should equal 44

#how_many_bees3(hive)

######
def rotated(table):
    rotated_table = []
    for x in range(len(table[0])):
        column = get_column(table, x)
        rotated_table.append(column)

    #print(rotated_table)
    return rotated_table

def get_column(table, x):
    column = []
    for row in table:
        value = row[x]
        column.append(value)
    print(column)
    return column

hive4 = ["abcde",
        "12345",
        "xXxXx"]

rotated(hive4)

def rotated2(table):
    rotated_table = []
    for x in range(len(table[0])):

        rotated_row = []
        for row in table:
            rotated_row.append(row[x])

        rotated_table.append(rotated_row)

    return rotated_table

def rotated3(table):
    rotated_table = []
    for x in range(len(table[0])):

        rotated_row = []
        for row in table:
            rotated_row.append(row[x])

        rotated_table.append("".join(rotated_row))

    return rotated_table

def rotated4(table):
    rotated_table = []
    for x in range(len(table[0])):
        rotated_table.append("".join(row[x] for row in table))
    return rotated_table


table = [
    ['b', 'e', 'e', '.'],
    ['.', 'e', '.', '.'],
    ['.', 'b', '.', '.'],
]

for row in rotated(table):
    print(row)