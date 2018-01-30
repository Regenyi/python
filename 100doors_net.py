# original:

# doors = [False] * 100
# for i in range(100):
#    for j in range(i, 100, i+1):
#        doors[j] = not doors[j]
#    print("Door %d:" % (i+1), 'open' if doors[i] else 'close')


#norbied v1:

doors = [False] * 100
for kör in range(100):
   for ajto_es_index in range(kör, 100, kör+1):
       doors[ajto_es_index] = not doors[ajto_es_index]

for index in range(100): 
    if doors[index]:
        status = 'open'
    else:
        status = 'close'

    print("Door {}: {}".format(index+1, status)) #itt a +1 hogy ne nullától kezdje, hanem egytől



