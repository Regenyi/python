doors = [0]*10 
rounds = 0
step = 1

def which_doors_to_change(ajto, lepes):
    indexes = list(range(len(doors)))
    if step == 1:
        return indexes
    else:
        return indexes[step-1::step]

while rounds < 10:
    for n in which_doors_to_change(doors, step):
        if doors[n] == 1:
            doors[n] = 0 
        else:
            doors[n] = 1
    rounds += 1
    step +=1 

# alternativa:
# for step in range(1, 100+1):
#     for i in which_doors_to_change(doors, step):
#        doors[i] = not doors[i]

for index, door in enumerate(doors):
#    print(index+1, door)
    print("Door", index+1, ":", door)
