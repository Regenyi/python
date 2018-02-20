import sys

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
# with open("ideas.txt","r") as ideabank:
#     print(list(ideabank)[-1])
#     lines = ideabank.readlines()
#     lines = lines[:-1]
#     #print(lines, file="ideas.txt")
#     ideabank.close()   
    # f = open('file1.txt').readlines()
    # open('file1.txt', 'w').writelines(lines[4:])

f = open("ideas.txt", "r")
listairó = []
for sor in f:
    listairó.append(sor.strip())
f.close()

if sys.argv[1] == "--list":
    for sor in listairó:
        print(sor)

#if sys.argv[1] == "--delete"

w = open("ideas2.txt", "w")
listairó = listairó[:-1]
for elem in listairó:
    print(elem, file=w)
w.close()


