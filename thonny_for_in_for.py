def rotated2(table):
    rotated_table = []
    for ELEM in range(len(table[0])):

        rotated_row = []
        for row in table:
            rotated_row.append(row[ELEM])

        rotated_table.append(rotated_row)

    return rotated_table

hive4 = ["abc",
         "123"]

rotated2(hive4)