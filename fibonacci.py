def fibonacci():
    Fiblist = [1,1]
    EndNumber = input("Enter the desired number:")

    Counter = 1
    while Counter <= int(EndNumber):
        Last = Fiblist[-1]
        BeforeLast = Fiblist[-2]
        LastTwo = Last + BeforeLast 
        Fiblist.append(LastTwo)
        Counter += 1 

    print("Fibonacci sequance:")
    print(*Fiblist,sep='\n') #asterx = keyword only, but i don't understand why it breaks the sequences into lines

fibonacci()