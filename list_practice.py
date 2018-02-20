#################
# funcitons / függvények
################


# import math
# def hypotenuse(x, y):
#     print(math.sqrt((x*x)+(y*y)))
# hypotenuse(2,8.5)

import math
def hypotenuse(x, y):
    if x == None:
        raise ValueError (".......")
    return (math.sqrt((x*x)+(y*y)))

print(hypotenuse(0, 8.5))


# def func_a():
#     print("message")
# func_a()
# b = func_a
# b()


# def hello_func(greetings, name="default"):
#     return ("{}, {}".format(greetings, name))

#print(hello_func('hi', 'Kalma'))


# def student_info(*barmi, **akarmi):
#     print(barmi)
#     print(akarmi)

#student_info("23", "abc", age=25, name="Jani" )


#################
# String excercide 6 http://python-textbok.readthedocs.io/en/1.0/Collections.html#exercise-6
################

my_list = [1, 1, 2, 3, 3]
c = set(my_list)
d = list(c)
e = list(range(1, 11))
f = {'1': '2', '3': '4', '5': '6'}
t = tuple(f.items())
v = list(f.values())
s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))
w = "the quick brown fox jumped over the lazy dog".split(" ")
# print(w)

#################
# Iterables, iterators
################

# forral 1-10 összeadása
# total = 0
# for i in range(10):
#     total = total + i
#     i += 1
# print(total)
# print(sum(range(10)))


# egy = 1
# factorial = int(input("integer?: "))
# for elem in range(1,factorial+1):
#     egy = egy * elem
# print(egy)

# counter = 1
# prod = 1
# #floaty = 0
# total = 0
# for elem in range(10):
#     floaty = int(input("please input nr {} of 10: ".format(counter)))
#     elem += 1
#     counter += 1
#     total = total + floaty
#     prod *= floaty

# avg = total/10
# print("sum: {} avg: {} product: {}".format(total,avg,prod))

# answers = []
# total = 0
# prod = 1
# for elem in range(1,10):
#     answer = input("number {}: ".format(elem))
#     answers.append(answer)
#     elem += 1

# answers = list(map(int, answers))

# for answer in answers:
#     total += int(answer)
#     prod *= answer
#     answer += 1

# print("sum: {}, prod: {}".format(total,prod))


# import random
# counter = 1
# x = random.randrange(1,6,1)
# hit_list = ['word', 'second','third','forth','fifth','sixth']
# hit = hit_list[x]
# print(hit)
# while counter < 10:
#     guess = input("Guess the number between 1-10!")
#     if guess == hit:
#         print("you guessed right! the secret word was: ", hit)
#         break
#     if x < 5 and guess != hit:
#         print("lower")
#         print("you guessed {} times out of 10".format(counter))
#     if x > 5 and guess != hit:
#         print("higher")
#     counter += 1


# lista=[]
# number = 0
# total = 0
# while total < 200:
#     number += 1
#     total += number**2
#     lista.append(number**2)
# print()
# print(total)
# print(lista)

animals = ['cat', 'dog', 'fish']

animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']
animals_set = set(animals)
print(animals_set)

# for first_animal in animals:
#     for second_animal in animals:
#         print("Yesterday I bought a %s. Today I bought a %s." % (first_animal, second_animal))


# x = 0
# while x < 10:
#     if x == 4:
#         print("Found!")
#     print(x)
#     x += 1

##################
# list practice
##################

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
timetable = [[""] * 24 for day in range(7)]
timetable[1][7] = "meeting"
for day_index, day in enumerate(timetable):
    day_name = WEEKDAYS[day_index]
    for i, event in enumerate(day):
        if event:
            print("%s at %02d:00 -- %s" % (day_name, i, event))


#calendar = [[[""]*7 for weeks in range(4)]*1 for months in range(12)]

#calendar[1][14] = "meeting"
# print(len(calendar))

my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

my_table[0][0] = 42
# print(my_table)

# print(my_table[0][0]) #nincs vessző közöttük!!!!

my_3d_list = [[[1, 2], [3, 4]],
              [[5, 6], [7, 8]], ]

# print(my_3d_list[1][0][0])

day = [""] * 24
week = [[""] * 24 for day in range(7)]
week[0][15] = "meeting"
# print(week)


# a = [("single_element"),(2,3),(1,2,3)]
# print(a)
# b = [list(range(10)),[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# print(b)
# print(b[0][1:-1])


nums = [1, 2, 4, 6, 7, 9]
key = 3
lista = [k+key for k in nums]
# print(lista)
res = (n*n for n in nums)
# for i in res:
#    print(i)


# my_list = ["Fanny", "Marci", "Aron"]

# list2 = my_list[:]

# my_list.extend(["Meg", "allatok"])

# list2.insert(2,"fib")

# del list2[1]

# my_list.remove("Aron")

# print(my_list.index("Marci"))
# print(my_list.sort(key=str.lower))
# print(list2)
# print(list2.count("fib"))

# a = [1,3,5]
# b = [2,4,6]
# c = a + b
# d = sorted(c) #sorted copy of c, leaving c unchanged.
# d.reverse()
# c.insert(3,42)
# d.append(10)
# c.extend([7,8,9])

# print(c[:3])
# print(d[-1])
# print(len(d))

############
# újrairások
############

# import csv
# with open('file.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

#(n for n in nums())
