def fibonacci():

    FibList = [1,1]
    EndNumber = input("Enter the desired number:")     
    while int(EndNumber) >= 30:   
        print("Please give a number under 30!")
        EndNumber = input("Enter the desired number:") 
 
    Sequence = []
    Counter = 1
    while Counter <= int(EndNumber):      
        Last = FibList[-1]
        BeforeLast = FibList[-2]
        LastTwo = Last + BeforeLast 
        FibList.append(LastTwo)
        Sequence.append(Counter) #miért nem rakja bele sorba?
        Counter += 1
    
    #dinamikus "karakterkiegészités"
    MaxLength = len(str(max(FibList))) #-1 hogy ne fusson túl?
    Expansion = "_"
    Newlist = []
    i = 1
    while i < int(EndNumber):
        LengthN = len(str(FibList[i]))
        SpacesNeeded = MaxLength - LengthN 
        Prefix = SpacesNeeded * Expansion   
        Newlist.append(str(Prefix) + str(FibList[i]))
        i += 1
    
    #print it   
    print("Fibonacci sequence:")     
    for i, Item in enumerate(Newlist):
        print('{:>3}. : {:>8}'.format(i+1, Item))
        #print('{:>3}. : {:>{MaxLength}}'.format(i+1, item, MaxLength=MaxLength))
     
fibonacci()


