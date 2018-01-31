# RA CC Dojo 2 TW python

numbers = [-5, 2300, 0, -9, 1200, 99, 105, -43, 500, 10000, 12000]
print(numbers)
j = 0
k = 0
i = 1

max_value = numbers[j]
min_value = numbers[j]

while i < len(numbers):
#for i in range(1, len(numbers)):
    if max_value < numbers[j+1]: 
        max_value = numbers[j+1]
    else:
        j = j+1
    i += 1

for i in numbers:
    if min_value > numbers[k+1]:
        min_value = numbers[k+1]
    else:
        k = k+1

avarage = (abs(min_value) + abs(max_value))/2

print(max_value)
print(min_value)
print(avarage)


# min = numbers[0]
# for num in numberS:
#         if min > num:
#             min = num
  
# Sorting draft:
    # if numbers[j] < numbers[j+1]:
    #     temp = numbers[j+1]
    #     numbers[j+1] = numbers[j]
    #     numbers[j] = temp
    # j = j+1

# print("max is:", numbers[-1])
# print("min is:", numbers[1])
# avarage = abs((numbers[-1]) + abs(numbers[1]))/2 
# print("avrg is:", avarage)