# Add a try-except statement to the body of this function which handles a possible IndexError, \
# which could occur if the index provided exceeds the length of the list. \
# Print an error message if this happens:

lista = [1,2,3,4]

def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Nagyobb az index, mint amennyi elem van!")

#print_list_element(lista,4)

n = False
while n == True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Hey, that wasn't a number!")
    else:
        print("I see that you are %d years old." % age)
    finally:
        print("It was really nice talking to you. Goodbye!")