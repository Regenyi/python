#doors = [0]*10

# for i in range(10):
#     n = 0
#     for door in doors:
#         if doors[n] == 1:
#             doors[n] = 0
#         else:
#             doors[n] = 1
#         n += 1
#     print (doors) 

#The following doors are open:

doors = [0]*10 #list(range(2, 102, X)) #print basic-be!!!
X = 1
rounds = 0

while rounds < 2:
    n = 0
    for door in doors[::X]:
        if doors[n] == 1:
            doors[n] = 0 
        else:
            doors[n] = 1 
        n += 1
    rounds += 1
    X +=1 

for index, door in enumerate(doors):
#    print(index+1, door)
    print(index+1, "th door is ", door, sep='')

#doors = [False] * 100
# for i in range(100):
#    for j in range(i, 100, i+1):
#        doors[j] = not doors[j]
#    print("Door %d:" % (i+1), 'open' if doors[i] else 'close')


# for door in doors:  
#     if door == "closed":
#         door = "open" 
#     else:
#         door = "closed"

# for mindenmásodik door in doors:


#menj végig az összes ajtón
#ha be van zárva nyisd ki 
#ha ki van nyitva zárd be 
#ha végig mentél menj az elejére 

#menj végig minden második ajtón
#ha be van zárva nyisd ki 
#ha ki van nyitva zárd be 
#ha végig mentél menj az elejére 

#menj végig minden harmadik ajtón
#ha be van zárva nyisd ki 
#ha ki van nyitva zárd be 
#ha végig mentél menj az elejére 







