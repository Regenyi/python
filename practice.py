
print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")


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
