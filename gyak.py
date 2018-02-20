import time
import pprint

#Írd ki a táblát a csapatok neve szerint ABC-sorrendben!
rendezett = []
tábla = open("temp.txt")
for sor in tábla:
    rendezett.append(sor.split(":"))
tábla.close()

for i in sorted(rendezett):
  print(i[0])

print(rendezett)
# columns = list(zip(*rendezett))
# print(columns[0])


# # print(sorted(rendezett))
# pprint.pprint(sorted(columns[0]))
    







#rendezés
# lista = [66, -45,-12,99,34,-1,5,8,4]
# print(sorted(lista, key=abs, reverse=True))            

# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if lista[i] > lista[j]:
#             lista[i], lista[j] = lista[j], lista[i]

# lista2 = lista
# lista2.sort(key=abs)
# print(lista2)

#F0025d: Hozz létre egy 100 elemű listát 0 és 100 közötti számokból! 
# Mennyi belőle összesen a 30-nál kisebb  és a 60-nál nagyobb szám?
# counter = 0
# lista = ["piros", "zöld", "kék", "kék", "piros", "zöld", "sárga", "kék", "piros"] 
# for i in lista:
#     if i == "piros" or i == "kék":
#         counter +=1

# print(lista.count("piros") + lista.count("kék"))
# print(counter)


#F0025b: Dobj fel egy kockát 100000-szer, a dobásokat tárold listában! Hány hatosod van? (Megoldás itt.)
# dobások = []
# hatos = 0

# for dobás in range(100):
#     dobás = random.randint(1, 6)
#     dobások.append(dobás) 
#     if dobás == 6:
#         hatos += 1

# print(dobások.index(6))

# for i,v in enumerate(dobások):
#     if v == 6:
#         print("a", i, ". hatos")

# print("hatosok száma: ", hatos)


# F0027c: Írj olyan függvényt, ami az átadott számnál eggyel nagyobbat ad vissza! A használatával 
# írasd ki az első száz pozitív egész számot és az eggyel nagyobb szomszédjukat

# vezérek = ['Adam', 'Bence', 'Tasziló']
# kit = input("kit keresel? ")
# for i,a in enumerate(vezérek):
#     if a == kit:
#         print(kit,"az", i+1, ". vezér")

# n = [5,3,25]
# xx = list(map(lambda x: x**2,n))
# print(xx)

#y = lambda x: x*2
#print(y(55))



#Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként
# egy másik fájlba!

# fájl = open('temp.txt')
# lista = []
# for sor in fájl:
#     lista.append(sor.strip())

# fájl.close()

# print(" ".join(lista), " \n", end="")




#Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
# fájl = open('temp.txt')
# lista = [] 
# for sor in fájl:
#     sor_hántolt = (sor.strip())
#     lista.append(sor_hántolt)

# fájl.close() 

# print(" ".join(lista) , "\n", end="")


# #Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget, 
# # hanem minden sort azonnal kiírsz! 
# egybe_fájl = open('temp.txt', 'r')
# for sor in egybe_fájl:
#     print(sor.strip(), end="" )
# egybe_fájl.close()
