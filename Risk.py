'''Write a python script, that generates 5 numbers between 1 and 6 and prints them 
in a meaningful way for the game. Sort the results for the attacker and for the defender, 
so make roll pairs, like in this image:
In a dice pair, there are the following rules:

Dice:
  Attacker: 5-4-1
  Defender: 6-2
'''

import random

def risk():
    print("Dice:")
    #attacker  
    v1 = random.randrange(1,6)
    v2 = random.randrange(1,6)
    v3 = random.randrange(1,6)
    print ("    Attacker:", v1,"-",v2,"-",v3)

    #defender =
    v4 = random.randrange(1,6)
    v5 = random.randrange(1,6)
    print ("    Defender:", v4,"-",v5)

    '''megtalálni a legnagyobb számot, azt összevetni a legnagyobbal
* When the attacker's die value is larger: Attacker wins (1 defender unit dies)
* When the 2 dice value is tie: Defender wins (1 attacker unit dies)
* When the defender's die value is larger: Defender wins (1 attacker unit dies)
    '''

    #sorted(templist, key=int, reverse=True)

    x = v1 - v4
    y = v2 - v5

    print("\n Outcome:")
    print("    Attacker: Lost", x, "unit")
    print("    Defender: Lost", y, "unit")

risk()