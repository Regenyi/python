# list practice

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

a = [1,3,5]
b = [2,4,6]
c = a + b
d = sorted(c) #sorted copy of c, leaving c unchanged.
d.reverse()
c.insert(3,42)
d.append(10)
c.extend([7,8,9])

print(c[:3])  
print(d[-1])  
print(len(d))  