import sys

with open("test.txt","a") as ideabank:
    idea = input("what is your new idea?")
    ideabank.write(idea + "\n") 
    ideabank.close() 

with open("test.txt","r") as ideabank:
    for i, line in enumerate(ideabank):
        print('{}.{}'.format(i+1, line.strip()))
        #print (ideabank.read())
    ideabank.close() 

