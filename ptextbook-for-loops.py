############
# 2: for loops
############

# pets = ["fanny", "marci", "findusz"]
# for i, pet in enumerate(pets):
#     i = pet.upper()
#     print(i)
#    print(pet)
#    pets[i] = pet.upper()
#print(pets)


# 2/1: sums the integers from 1 to 10 with for
# summ = 0
# for num in range(1,11):
#     summ += num
#     print(num) 
# print("for:",summ)


# 2/2:
# print(sum(range(1,11)))


# 2/3: Write a program which finds the factorial of a given number. 
# E.g. 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is equal to 5 x 4 x 3 x 2 x 1,
# def fact(num):
#     fact = 1
#     for elem in range(1,num+1):
#         fact *= elem
#     print(fact)
# fact(5)


# 2/4: Write a program which prompts the user for 10 floating-point numbers and calculates 
# their sum, product and average. Your program should only contain a single loop.

# i = 1
# summ = []
# product = 1
# while i <= 2:
#     b = float(input("float nr {}? ".format(i)))
#     summ.append(b)
#     product *= b 
#     i += 1 
# print(sum(summ))
# print(sum(summ)/2) 
# print(product)


# 2/5: Rewrite the previous program so that it has two loops – one which collects 
# and stores the numbers, and one which processes them.

# i = 1
# nums = []
# summ = 0
# prod = 1
# while i <= 3:
#     nums.append(float(input("number {} ".format(i))))
#     i += 1
# for num in nums:
#     summ += num
#     prod *= num
# print(summ)
# print(summ/len(nums)) 
# print(prod) 


############
# 3: nested loops
############

CALENDAR = 'projekt' 

# first let's define weekday names
timetable = [[""] * 24 for d in range(7)] 
timetable[0][15] = "Ez az elfoglaltság helye"
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# now we iterate over each day in the timetable
# Itt a day az egy tömb, a weekdays index-nek pedig int kellene. Szóval itt is használj enumerate-et, hogy legyen day indexed.
for i, day in enumerate(timetable):
    print(day)
    day_name = WEEKDAYS[i]
    for i, event in enumerate(day):
        if event:
            print("%s at %02d:00 -- %s" % (day_name, i, event))

