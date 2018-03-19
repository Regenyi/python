lista = [1,92,32,4,35,7,11,]

for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        print(lista[i], "-t hasonlitom össze ", lista[j], "-vel", sep="")
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(lista)
#print(sorted(lista))


#fogom a rendezendő listát 
#összehasonlitom az első elemét, a másodikkal és ha nagyobb, akkor megcserélem
# aztán lépek egyet az indexben és összehasonlitom a következővel egészen a lista végéig.
 
