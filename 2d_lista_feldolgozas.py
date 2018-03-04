#Az előző megoldásodat alakítsd át úgy, hogy használj függvényt, \
# és a függvény akármelyik poszton játszó játékosokat meg tudja számolni. 
# A függvény két paramétere a 2D lista, illetve a megszámolandó játékosok posztja.
# Ki és milyen poszton rúgta a legkevesebb gólt? Tipp: határozd meg, hogy mennyi a legkevesebb gól, aztán határozd meg, hogy ki rúgott ennyit.
# F0029e: Van-e olyan, aki legalább 10 meccset játszott?
# F0029f: Hány gólt rúgtak a játékosok átlagosan? Tipp: számold össze a gólokat, majd a kapott számot oszd el a focisták lista hosszával!
# F0029g: Hány gólt rúgtak az egyes posztokon lévő játékosok átlagosan?  

focisták = []
fájl = open("temp.txt") 
for sor in fájl:
    focisták.append(sor.split())
fájl.close()

def legkevesebb_gól(lista):
    számláló2 = 100
    for gól in lista:
        if int(gól[3]) < számláló2 : 
            számláló2 = int(gól[3])
    return számláló2

def kirúgott_ennyi_gólt(lista, gól):
    vissza = [] #cut
    for elem in lista:
        if elem[3] == str(gól):
            #return elem[0] #insert
            vissza.append([elem[0],elem[1]]) #igy lehet két elemet
    return vissza

# counter = 0
# gólok = []
# for sor in focisták:
#     gólok.append(int(sor[3]))
# print(sum(gólok)/len(gólok))
# print(sum(gólok))

def számoló(lista, poszt):
    számláló = 0
    for játékos in lista:
        if játékos[1] == poszt:
            számláló += 1
    return számláló

# for poszt in ["kozeppalyas", "csatar", "hatved", "deger"]:
#     print("ennyi:", poszt, számoló(focisták,poszt))

print(legkevesebb_gól(focisták))
print(kirúgott_ennyi_gólt(focisták, legkevesebb_gól(focisták)))

for sor in (kirúgott_ennyi_gólt(focisták, legkevesebb_gól(focisták))):
    print(sor)
    print(' a '.join(sor))
