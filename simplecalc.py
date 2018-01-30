#Regényi Ádám / CC , Python 1st SI Assignment 

while True: 

    nr1 = input("Enter a number (or a letter to exit:) ")
    if nr1.isdigit(): 
        nr1int = int(nr1)
    else:
        exit()

    list1 = ["+", "-", "*", "/"]
    operation = input("Enter an operation (+, -, *, /) : ")
    while operation not in list1: #"+" or "-" or "/" or "*" 
        operation = input("Please enter an operation (+, -, *, /) : ")            

    nr2 = input("Enter another number: ")
    while nr2.isdigit() == False :  
        nr2 = input("Please enter another number: ")   
    while nr2 == "0": 
        print("You can't divide by zero!")
        nr2 = (input("Enter another number: "))

    if operation == "+":
        result = int(nr1) + int(nr2)         
    if operation == "-":
        result = int(nr1) - int(nr2)
    if operation == "*":
        result = int(nr1) * int(nr2)
    if operation == "/":
        result = int(nr1) / int(nr2) #when the result is an integer it will still display #.0  

    print("Result:", (result))

