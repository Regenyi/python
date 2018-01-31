#################
# Tips, Tricks
################
https://docs.python.org/3.1/library/string.html#format-specification-mini-language
http://pythontutor.com/visualize.html#mode=edit
https://www.cheatography.com/davechild/cheat-sheets/python/pdf_bw/
http://python-textbok.readthedocs.io/en/1.0/Selection_Control_Statements.html

if n%2 == 0: #párosszámok 
Strings are objects! -> "{0}'s password is {1}".format(username, password)
 print("Door {}: {}".format(index, status))

 format(value, '.6f')  #kerekités 
Bytes are not characters; bytes are bytes. Characters are an abstraction. A string is a sequence of those abstractions.  

#in, not in
if number in numbers:
	print("%d is in the list!" % number)
my_number = 90
if number not in numbers:

    # the sum of a list of numbers
sum(numbers)
# are any of these values true?
any([1,0,1,0,1])
# are all of these values true?
all([1,0,1,0,1])

#összeadás for looppal 
lista = [1,2,3,4,5,6]
total = 0
for elem in lista:
	total = total + elem
print(total)

a Classok nagybetűvel kezdődnek
a global-ok meg csupa nagybetű 


#################
# IMMUTABLE objects
################
    Set
    Byte 

#################
# LIST
################


list(range(2, 102, X)) #100 szám 2-102 között, X lépéssel
pets = animals[:] # assign a *copy* of animals to pets
animals.append('aardvark')


#################
# SET
################

.difference()
.union()
set{} = #emptyset
set.intersection()

#################
# GENERATORS
################

nums = [1,2,3,4]
my_list = [n for n in nums] = 1,2,3

#################
# DICTIONARY
################
dict = {'key1':'Value'....}
print(dict['key1']] #fentit fogja kinyomtatni
dict.get() 
dict.values()
dict.keys()
dict.items()
dict['newkey'] = 'Value2'
del dict['key']
dict.pop('age')
dict.update({'key3': ... , ...})

for key,value in dict.items():
    print(key,value)


#################
# GIT
################
git config --global user.name "name"
git config --list
Git init
git clone http dir
git --version
git add -A 
git commit -m "komment"
git push
git pull
git branch
git merge 
Index = staging  