import sys
import argparse

parser = argparse.ArgumentParser()

# with open("test.txt","a") as ideabank:
#     idea = input("what is your new idea?")
#     ideabank.write(idea + "\n") 
#     ideabank.close() 

# with open("test.txt","r") as ideabank:
#     for i, line in enumerate(ideabank):
#         print('{}.{}'.format(i+1, line.strip()))
#         #print (ideabank.read())
#     ideabank.close() 

#--delete 1
with open("test.txt","r") as ideabank:
    print(list(ideabank)[-1])
    lines = ideabank.readlines()
    lines = lines[:-1]
    ideabank.close()   
    # f = open('file1.txt').readlines()
    # open('file1.txt', 'w').writelines(lines[4:])

#--list 
