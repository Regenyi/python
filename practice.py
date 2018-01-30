

'''
#Each floating-point number should be formatted that only the first two decimal places are returned. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
#Don't round the numbers! Just cut them after two decimal places!

def two_decimal_places(number):
    sp1, sp2 = str(number).split('.')
    # number = '.'.join([sp1, sp2[0:2]])
    # number = float(number)
    number = float('.'.join([sp1, sp2[0:2]]))
    return number
print(two_decimal_places(34.5678))

#helyes megoldás: 
def two_decimal_places(number):
    return int (number * 100) / 100.0

'''

# correct_input = False
# while not correct_input:
#     try:
#         T_f = float(input("What Fahrenheit value do you want to convert to Celsius? "))
#     except ValueError:
#         print("Wrong format!")
#     else:
#         correct_input = True

# T_c = (5/9) * (T_f - 32) #T_c is the temperature in °C and T_f is the temperature in °F

# print("In Celsius it is: ", T_c)
# a = 5
# def my_func(my_var):
#     a = 8 + my_var
#     my_var = a

# my_func(25)
# print(a)

# good_format = False
# while good_format == False:
# while not good_format:

#     try:
#         F_c = float(input("input?"))
#     except ValueError:
#         print("wrong format")
#     else:
#         good_format = True
