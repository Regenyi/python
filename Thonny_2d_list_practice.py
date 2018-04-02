##a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
##s = 0
##for i in range(len(a)):
##    for j in range(len(a[i])):
##        s += a[i][j]
##print(s)

def which_year_max(table):
    for sor in range(1, len(table)):
        for elem in sor: 
            if elem[3] == sor[-1][3] and elem[4] == 'in':
                print(elem[3],sor[-1][3],elem[4])

table = [['kH14Ju#&', '1', '21', '2016', 'in', '31'], ['kH38Jm#&', '10', '23', '2016', 'out', '40'], ['eH34Jd#&', '2', '12', '2016', 'in', '400']]
which_year_max(table)