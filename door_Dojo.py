door=[]
final=[]

for i in range(0,100):
    door.append('x')

print(door)    

print("\n")
for j in range(1,101):
    for i in range(j-1,100,j):
        if door[i]=="x":
           door[i]="o"
        elif door[i]=="o":
           door[i]="x"

print(door) 

for k in range(0,100):
    if door[k]=="o":
        final.append(k+1)          

print("\n",final)        