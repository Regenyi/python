def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]  # kiolvassa hogy a dict-ben benne van-e a listname-nevű kulcs (ha nem sikerül jön az exception) és l nevű változoként deklarálja ezt
    except KeyError:  #ha kulcs hiba van, azaz nincs benne a dictben, akkor:
        thedict[listname] = [] # üres tömb értéket ad a listname kulcsnak,
        print("Created %s." % listname) #kiirja, hogy belerakta a konkrét lista nevet, 
    else: # ha nem volt exception, akkor: 
        print("%s already has %d elements." % (listname, len(l))) # printelje ki, hogy kulcsban, hány lista elem volt.
    finally: # ezt mindenképpen: 
        thedict[listname].append(element) #rakd bele a kulcsnévhez az elemet  
        print("Added %s to %s." % (element, listname)) #kirja, hogy hány elemet adott a kulcsnévhez.

months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : ["May","Cucc"], 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }

add_to_list_in_dict(months, 13, "ceger")
print(months)
  