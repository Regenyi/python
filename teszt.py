import pprint
# i = "1"
# print(i)
# allowed_chars = ["A1","B1"]
# print(allowed_chars)

# while True: 
#     try:
#         user_input = input("target?")
#     except:
#         print("wrong format")
#     if user_input in allowed_chars:
#     #if user_input == allowed_chars[0] or user_input == allowed_chars[1] :
#         print("x")
#         break
#         # row1[0] = ("\033[1;32;40mX\033[0m")x

primes = [1,3,5,6]
primes.append(3)
board_player = [[0 for x in range(6)] for y in range(6)]
allowed_chars = [(x, y) for x in range(6) for y in range(6)]
pprint.pprint(allowed_chars)
print(allowed_chars[2:5])
dir(primes)
#help(primes.reverse)