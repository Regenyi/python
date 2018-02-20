# Globals:
re = ("\033[0;37;41m  \033[0m")
bl = ("\033[0;37;40m  \033[0m")


board_ai = [
    [bl, bl, bl, bl, bl, bl],
    [re, re, re, re, re, re],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

z = 4
y = list(range(z))
maxlength = 1.8*z
maxlength2 = "".join(["  ", ("--"*z+"-")*6])
space = " "


def print_board():
    # ai:
    print ("Computer: \n".center(len(maxlength2)))
    print('{0:>{width}}A {0:>{width}}B {0:>{width}}C {0:>{width}}D {0:>{width}}E {0:>{width}}F'.format(space, width=maxlength))
    for i in y:
        print("".join(["1 ", board_ai[0][0]*z+"|", board_ai[0][1]*z+"|", board_ai[0][2]
                       * z+"|", board_ai[0][3]*z+"|", board_ai[0][4]*z+"|", board_ai[0][5]*z+"|"]))
    print("".join(["  ", "--"*z+"-", "--"*z+"-", "--"*z+"-", "--"*z+"-", "--"*z+"-", "--"*z+"-"]))
    for i in y:
        print("".join(["2 ", board_ai[1][0]*z+"|", board_ai[1][1]*z+"|"]))
    print("")


print_board()
