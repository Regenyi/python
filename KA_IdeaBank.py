"""This application saves
the given text into a local file.

It saves the new idea by appending it
to the file, to allow multiple ideas to be saved.
After saving the idea,
it shows the existing ideas.

ideabank.txt was created by running
the following code once:
my_file = open("ideabank.txt", "w")
my_file.close()
"""

my_file = open("ideabank.txt", "r")
RL_list = my_file.readlines()
lenRL = len(RL_list) + 1
lenRLstr = str(lenRL)
my_file.close()

my_file = open("ideabank.txt", "a")
idea = input("What is your new idea: ")
my_file.write(lenRLstr + ". " + idea + "\n")
my_file.close()

my_file = open("ideabank.txt", "r")
print("\nMy ideabank:")
print(my_file.read())
my_file.close()
