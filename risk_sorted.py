'''Write a python script, that generates 5 numbers between 1 and 6 and prints them 
in a meaningful way for the game. Sort the results for the attacker and for the defender, 
so make roll pairs, like in this image:
In a dice pair, there are the following rules:
* When the attacker's die value is larger: Attacker wins (1 defender unit dies)
* When the 2 dice value is tie: Defender wins (1 attacker unit dies)
* When the defender's die value is larger: Defender wins (1 attacker unit dies '''


import random

def risk():
    AttackerScore = 0
    DefenderScore = 0
    print("Dice:")
    #attacker  
    v1 = random.randrange(1,6)
    v2 = random.randrange(1,6)
    v3 = random.randrange(1,6)
    attacker = [v1,v2,v3]
    attacker.sort(key=int, reverse=True)
    v1 = attacker[0]
    v2 = attacker[1]
    v3 = attacker[2]
    print ("    Attacker:", v1,"-",v2,"-",v3)

    #defender =
    v4 = random.randrange(1,6)
    v5 = random.randrange(1,6)
    defender = [v4,v5]
    defender.sort(key=int, reverse=True)
    v4 = defender[0]
    v5 = defender[1]
    print ("    Defender:", v4,"-",v5)

    x = v1 - v4
    if x > 0:
        AttackerScore = 0
        DefenderScore = -1           
    elif x == 0:
        AttackerScore = 0
        DefenderScore = 0 
    else:
        AttackerScore = -1
        DefenderScore = 0 
        
    y = v2 - v5
    if y > 0:
        AttackerScore = 0
        DefenderScore = -1           
    elif y == 0:
        AttackerScore = 0
        DefenderScore = 0 
    else:
        AttackerScore = -1
        DefenderScore = 0 

    print("\nOutcome:")
    print("    Attacker: Lost", AttackerScore, "unit")
    print("    Defender: Lost", DefenderScore, "unit")

risk()