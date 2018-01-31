import sys

if sys.argv == 2:
    with open("todo.txt","a") as todofile:
        todo = input("what is your task?")
        todofile.write(todo + "\n") 
        todofile.close() 

with open("todo.txt","r") as todofile:
    for i, line in enumerate(todofile):
        print('{}.{}'.format(i+1, line.strip()))
        print (todofile.read())
    todofile.close() 

# print ("Hello %s!" % sys.argv[1])

