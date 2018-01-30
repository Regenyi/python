### Assignment1: Simple Calculator

# Intro help
print("""This is a simple calculator.
Usage:
- First step: enter a rational number at the first prompt
- Second step: enter one of the following operators at the second prompt
    - for subtraction
    + for addition
    * for mmultiplication
    ** for exponentiation
    / for division
    // for integer division
    % (percentage sign) for modulo
- Third step: enter another rational number at the 3rd prompt
- Fourth step: see result.
""")

while True:
    # Exception handling user input for 1st number: ValueError
    num1f = None
    while type(num1f) != float:
        num1s = input("Enter a rational number (exit: Ctrl+Z): ")
        try:
            float(num1s)
            num1f = float(num1s)
        except ValueError:
            print("\n" + num1s, "is not a rational number.\nTry again!")
        except:
            print("Unexpected error.")
    print("You entered:", num1f)

    # Exception handling user input for operator: AssertionError
    print("""You can use the following operations:
    - for subtraction
    + for addition
    * for mmultiplication
    ** for exponentiation
    / for division
    // for integer division
    % (percentage sign) for modulo
    """)

    oper = "***"
    OperList = "-, +, *, **, /, //, %"
    while oper not in OperList:
        try:
            oper = input("Enter an operator: ")
            assert (oper in ("-", "+", "*", "**", "/", "//", "%"))
        except AssertionError:
            print("\nNot a valid operator.\n")
        except:
            print("Unexpected error.")
    print("You entered:", oper)

    # Exception handling user input for 2nd number: ValueError and ZeroDivisionError
    num2f = None
    while not((oper not in "/, //, %") or (num2f != 0)) or type(num2f) != float:
        num2s = input("Enter a rational number (exit: Ctrl+Z): ")
        try:
            float(num2s)
            num2f = float(num2s)
        except ValueError:
            print("\n" + num2s, "is not a rational number.\nTry again!")
        except:
            print("Unexpected error.\nTry again!")
        
        if oper == "/":
            try:
                float(num1f / num2f)
            except ZeroDivisionError:
                print("You cannot use 0 in the denominator with", oper, ".\nTry agan!")
            except ValueError:
                print("\n" + num2s, "is not a rational number.\nTry again!")
            except:
                pass
        
        if oper == "//":
            try:
                float(num1f // num2f)
            except ZeroDivisionError:
                print("You cannot use 0 in the denominator with", oper, ".\nTry agan!")
            except ValueError:
                print("\n" + num2s, "is not a rational number.\nTry again!")
            except:
                pass
        
        if oper == "%":
            try:
                float(num1f % num2f)
            except ZeroDivisionError:
                print("You cannot use 0 in the denominator with", oper, ".\nTry agan!")
            except ValueError:
                print("\n" + num2s, "is not a rational number.\nTry again!")
            except:
                pass
    print("You entered:", num2f)
    
    # Calculatiions:
    result = None
    if oper == "+":
        result = float(num1f + num2f)
    elif oper == "-":
        result = float(num1f - num2f)
    elif oper == "*":
        result = float(num1f * num2f)
    elif oper == "**":
        result = float(num1f ** num2f)
    elif oper == "/":
        result = float(num1f / num2f)
    elif oper == "//":
        result = float(num1f // num2f)
    elif oper == "%":
        result = float(num1f % num2f)
    else:
        result = "not defined"
        print("'" + oper + "'" + " is unknown")
    print("\nYour result is " + str(result) + "\n")
    print("Start over or press 'Ctrl + Z' to exit the program.")
