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

# conversions
animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']
animals_set = set(animals)
animals_unique_list = list(animals_set)
animals_unique_tuple = tuple(animals_unique_list)

#dictionary conv:
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
colours = list(marbles) # the keys will be used by default
counts = tuple(marbles.values()) # but we can use a view to get the values
marbles_set = set(marbles.items()) # or the key-value pairs

dict([(1, 2), (3, 4)]) # pairs can be converted to dict 
abc_list = list("abracadabra") #convert a string to a list of characters
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
s = "".join(l) #join l to string

print("cat, dog, fish".split(", ", 1)) #limit on the maximum number of splits

#2 dimenziós tömb:
week = [[""] * 24 for day in range(7)] 

ez egy tuple = [("single_element"),(2,3),(1,2,3)]
Tuples are fixed size in nature whereas lists are dynamic. In other words, a tuple is immutable whereas a list is mutable. 
You can't add elements to a tuple. Tuples have no append or extend method.

#függvény meghivása egy változóból
b = func_a
b()

#map, filet, reduce
list(map(c_to_f, temps)) #c_to_f = lambda data: (data[0], (4/5)*data[1]+32) 
list(map(lambda x: x > 5, data)) #van egy statistic.mean()-nel legenerált data listánk, abból leszűri az 5 fölöttieket
list(filter(None, lista_neve)) "", 0 ilyeneket kivág az adatból

# printing
Use the new-style string formatting:
print("Total score for {} is {}".format(name, score))
Use the new-style string formatting with numbers (useful for reordering or printing the same one multiple times):
print("Total score for {0} is {1}".format(name, score))
Use the new-style string formatting with explicit names:
print("Total score for {n} is {s}".format(n=name, s=score))

#################
# IMMUTABLE objects
################
    Set
    Byte 
    range is an immutable sequence type used for ranges of integers
    tuple 

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
my_list = [n for n in nums] #= 1,2,3,4

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

#ha van két külön, de azonos elemszánú lista/tuple, akkor zippel igy lehet belőlük dictinoary-t csinálni:
dic = dict(zip(month,days))


#################
# DECORATOR
################

shot from telefon 


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
van még a stash nevezetű dolog 

if you want to get a file from  another one  you have to do this:
- git commit -m "what you have done'
- git pull
- solve the merge conflicts
- git commit -> automatic merge confilict fixed message from git
- git push

#################
# NETWORK
################

PORT: Just as the IP address identifies the computer, The network port identifies the application or service running on the computer.
SOCKET: A socket is the combination of IP address plus port
SÜTI: Az eljárás célja az állapot bevezetése az alapvetően állapotmentes HTTP tranzakcióba, lokálisan jön létre
URL: webcím, pl https://hu.wikipedia.org:443/wiki 
    Ennek részei:
    A https a használandó protokoll. A protokoll neve után kettőspont (:) írandó.
    A hu.wikipedia.org a célgép tartományneve. Ez elé két perjel (//) írandó.
    A 443 a célgép azon hálózati portszáma, amin kérésünket várja; ez elé kettőspont (:) írandó. Ezt a részt gyakran teljesen elhagyhatjuk, például esetünkben a HTTPS protokoll alapértelmezett portszáma a 443.
    A /wiki a kért elérési út a célgépen. Ez a rész mindig a perjellel (/) kezdődik.
ROUTER: útválasztó, adatforgalom irányítása
TCP: helyes sorrend
IP: a gépi cim 
DNS: az emberi cim 
HTTP: "Hypertext Transfer Protocol". HTTP is a request/response protocol, your computer sends a request for some file, and the web server sends back a response.
HTTP REQUEST: 
    the IP address of you and/or your HTTP proxy
    which document you requested
    which version of which browser you're using
    which page you came from to get here (if you followed a link)
    your preferred language(s)
    cookies
USER AGENT: The request header field that delivers information about your browser and operating system 

#################
# VIRTUALENV
################

pip is a tool for installing packages from the Python Package Index.
virtualenv is a tool for creating isolated Python environments containing their own copy of python, pip, and their own place to keep libraries installed from PyPI.
It's designed to allow you to work on multiple projects with different dependencies at the same time on the same machine.
You can see instructions for installing it at virtualenv.org 
After installing it, run virtualenv venv to create a new environment inside a directory called venv.
You'll need one of these environments for each of your projects. Make sure you exclude these directories from your version control system.
To use the versions of python and pip inside the environment, type venv/bin/python and venv/bin/pip respectively.
You can "activate" an environment with source venv/bin/activate and deactivate one with deactivate. This is entirely optional but might make life a little easier.

############################
# FLASK PROJECT + VENV setup
############################

1. Create a project folder. 
2. Setup the magical virtualenv and activate it.
    "pip freeze" (You shall see a lot of packages. These are your globally installed packages)
    "virtualenv venv" (This will create a venv folder with a lot of Python stuff included. Even Python itself)
    "source ./venv/bin/activate" (And this "activates" the virtualenv in your current terminal window)
    "pip freeze" (You should see no packages. Because you have none installed yet in the virtualenv)
3. pip install Flask
4. Create the basic folder structure
    mkdir templates
    In your templates folder, create "index.html"