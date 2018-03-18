

# Extend the program in exercise 7 of the loop control statements chapter to include exception handling. 
# Whenever the user enters input of the incorrect type, keep prompting the user for the same value until it is entered correctly. 
# Give the user sensible feedback.

person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

def prop_query():
    for prop, p_type in properties:
        person[prop] = p_type(input("Please enter your {}: ".format(prop)))
#        ha az input type-ja nem p_type akkor kérdezd újra 


'''add_to_list_in_dict_orig function adds an element to a list inside a dict of lists. Rewrite it to use a try-except statement
which handles a possible KeyError if the list with the name provided doesn’t exist in the dictionary yet,
instead of checking beforehand whether it does. Include else and finally clauses in your try-except block:'''

def add_to_list_in_dict(thedict, listname, element):
    try:
        thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created {}.".format(listname))
    else:
        print("{} already has {} elements.".format(listname, len(thedict[listname])))
    finally:
        thedict[listname].append(element)
        print("Added {} to {}.".format(element, listname))

def add_to_list_in_dict_orig(thedict, listname, element):
    if listname in thedict:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)

    thedict[listname].append(element)

    print("Added %s to %s." % (element, listname))

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

# add_to_list_in_dict(months, 5, "ceger")
# print(months)


"""Add a try-except statement to the body of this function which handles a possible IndexError, 
which could occur if the index provided exceeds the length of the list. Print an error message if this happens:"""

def print_list_element_orig(thelist, index):
    print(thelist[index])

def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as ie:
        print("The list has no element at index %d." % index)
        #raise ie

lista = [1,2,3,4]
print_list_element(lista, 7)

