#100 doors nr.4

doors = [0] * 100
step = 1

def door_to_open(doors,step):
    indexes = list(range(len(doors))) #RANGE!!!!!!!!!!, hogy igazi számok legyenek, ne string!!!
    return indexes[step-1::step] #ezt nem értettem még mindig, átirva: végi megy a 100 számon a nulladik elemtől a végéig és annyit lép, amennyin a step van 

for step in range(1,100+1):
    for i in door_to_open(doors,step):
        doors[i] = not doors[i] #itt nem értem 
    step +=1 

for index in range(100): 
    if doors[index]:
        status = 'open'
    else:
        status = 'close'
    print("Door {}: {}".format(index+1, status))


# for i in range(1,100+1)
#     print("door", i : doors[step]  ) #itt se emlékeztem
#    status 'open' if door == 1 else 'close'


