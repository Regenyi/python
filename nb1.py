import pprint
nb1_állás = []
fájl = open("nb1.txt")
for sor in fájl:
    nb1_állás.append(sor.strip().split(":")) 

    sor = sor.strip().split(":")
    sor[1] = sor[1].split()

    táblasor = []
    táblasor.append(sor[0])
    táblasor.append(int(sor[1][0]))

fájl.close()

print(táblasor)
pprint.pprint(nb1_állás)