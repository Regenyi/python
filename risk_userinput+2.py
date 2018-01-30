# Risk literal version, needs optimalisation
import random
import re


def risk():
    AttackerScore = 0
    DefenderScore = 0

    answer1 = get_answer("how many attackers in the current roll?(1-3)")
    answer2 = get_answer("how many defenders in the current roll?(1-2)")

    # attacker:
    if answer1 == 1:
        roll1 = random.randrange(1, 6)
        attacker = [roll1]
        attacker.sort(key=int, reverse=True)
        roll1 = attacker[0]

    elif answer1 == 2:
        roll1 = random.randrange(1, 6)
        roll2 = random.randrange(1, 6)
        attacker = [roll1, roll2]
        attacker.sort(key=int, reverse=True)
        roll1 = attacker[0]
        roll2 = attacker[1]

    elif answer1 == 3:
        roll1 = random.randrange(1, 6)
        roll2 = random.randrange(1, 6)
        roll3 = random.randrange(1, 6)
        attacker = [roll1, roll2, roll3]
        attacker.sort(key=int, reverse=True)
        roll1 = attacker[0]
        roll2 = attacker[1]
        roll3 = attacker[2]

    # def get_attacker​_values(answer1):
    #     #...
    #     return roll1, roll2, roll3
    #     roll1, roll2, roll3 = get_attacker_values(answer1)

    # defender:
    if answer2 == 1:
        roll4 = random.randrange(1, 6)
        defender = [roll4]
        defender.sort(key=int, reverse=True)
        roll4 = defender[0]

    elif answer2 == 2:
        roll4 = random.randrange(1, 6)
        roll5 = random.randrange(1, 6)
        defender = [roll4, roll5]
        defender.sort(key=int, reverse=True)
        roll4 = defender[0]
        roll5 = defender[1]

    # AttackerScore, DefenderScore = calc_result(roll1 - roll4)​"""
    # AttackerScore, DefenderScore = calc_result(roll2 - roll5)​​"""

    print("Dice:")

    def results1():
        x = roll1 - roll4
        if x > 0:
            AttackerScore = 0
            DefenderScore = -1
        elif x == 0:
            AttackerScore = 0
            DefenderScore = 0
        else:
            AttackerScore = -1
            DefenderScore = 0

    if answer1 == 1 and answer2 == 1:
        results1()
        print("1")
        print("    Attacker:", roll1)
        print("    Defender:", roll4)
        print("\nOutcome:")
        print("    Attacker: Lost", AttackerScore, "unit")
        print("    Defender: Lost", DefenderScore, "unit")

    # elif answer1 == 1 and answer2 == 2:
    #     x = roll1 - roll4
    #     if x > 0:
    #         AttackerScore = 0
    #         DefenderScore = -1
    #     elif x == 0:
    #         AttackerScore = 0
    #         DefenderScore = 0
    #     else:
    #         AttackerScore = -1
    #         DefenderScore = 0
    #     print("1-2")
    #     print("    Attacker:", roll1)
    #     print("    Defender:", roll4,"-",roll5)
    #     print("\nOutcome:")
    #     print("    Attacker: Lost", AttackerScore, "unit")
    #     print("    Defender: Lost", DefenderScore, "unit")

    # elif answer1 == 2 and answer2 == 1:
    #     x = roll1 - roll4
    #     if x > 0:
    #         AttackerScore = 0
    #         DefenderScore = -1
    #     elif x == 0:
    #         AttackerScore = 0
    #         DefenderScore = 0
    #     else:
    #         AttackerScore = -1
    #         DefenderScore = 0
    #     print("2-1")
    #     print("    Attacker:", roll1,"-",roll2)
    #     print("    Defender:", roll4)
    #     print("\nOutcome:")
    #     print("    Attacker: Lost", AttackerScore, "unit")
    #     print("    Defender: Lost", DefenderScore, "unit")

    # elif answer1 == 2 and answer2 == 2:
    #     x = roll1 - roll4
    #     if x > 0:
    #         AttackerScore = 0
    #         DefenderScore = -1
    #     elif x == 0:
    #         AttackerScore = 0
    #         DefenderScore = 0
    #     else:
    #         AttackerScore = -1
    #         DefenderScore = 0

    #     y = roll2 - roll5
    #     if y > 0:
    #         AttackerScore2 = 0
    #         DefenderScore2 = -1
    #     elif y == 0:
    #         AttackerScore2 = 0
    #         DefenderScore2 = 0
    #     elif x < 0:
    #         AttackerScore2 = -1
    #         DefenderScore2 = 0
    #     print("2")
    #     print("    Attacker:", roll1,"-",roll2)
    #     print("    Defender:", roll4,"-",roll5)
    #     print("\nOutcome:")
    #     print("    Attacker: Lost", AttackerScore+AttackerScore2, "unit")
    #     print("    Defender: Lost", DefenderScore+DefenderScore2, "unit")

    # elif answer1 == 3 and answer2 == 1:
    #     x = roll1 - roll4
    #     if x > 0:
    #         AttackerScore = 0
    #         DefenderScore = -1
    #     elif x == 0:
    #         AttackerScore = 0
    #         DefenderScore = 0
    #     else:
    #         AttackerScore = -1
    #         DefenderScore = 0
    #     print("3-1")
    #     print ("    Attacker:", roll1,"-",roll2,"-",roll3)
    #     print ("    Defender:", roll4,)
    #     print("\nOutcome:")
    #     print("    Attacker: Lost", AttackerScore, "unit")
    #     print("    Defender: Lost", DefenderScore, "unit")

    # elif answer1 == 3 and answer2 == 2:
    #     x = roll1 - roll4
    #     if x > 0:
    #         AttackerScore = 0
    #         DefenderScore = -1
    #     elif x == 0:
    #         AttackerScore = 0
    #         DefenderScore = 0
    #     elif x < 0:
    #         AttackerScore = -1
    #         DefenderScore = 0

    #     y = roll2 - roll5
    #     if y > 0:
    #         AttackerScore2 = 0
    #         DefenderScore2 = -1
    #     elif y == 0:
    #         AttackerScore2 = 0
    #         DefenderScore2 = 0
    #     elif x < 0:
    #         AttackerScore2 = -1
    #         DefenderScore2 = 0
    #     print("3-2")
    #     print("    Attacker:", roll1,"-",roll2,"-",roll3)
    #     print("    Defender:", roll4,"-",roll5)
    #     print("\nOutcome:")
    #     print("    Attacker: Lost", AttackerScore+AttackerScore2, "unit")
    #     print("    Defender: Lost", DefenderScore+DefenderScore2, "unit")


def get_answer(question):
    answer = (input(question))
    while True:
        if len(answer) > 2:  # or (len(answer2) > 2):
            print("wrong format!")
            answer = (input(question))
        elif re.search("[a-z]", answer):
            print("wrong format!")
            answer = (input(question))
        else:
            break

    return int(answer)


risk()
