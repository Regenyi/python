Kérdések:
    # -

Amit nem tudok még:
    1# * git stash pontos használata, mikor és hogyan?
    2# dict comprehension trans = {char: n+1 for n, char in enumerate(string.ascii_lowercase)}
    3# cw feladat: 
    def bowling_pins(empty):
        raw =     ['I ', 'I ', 'I ', 'I\n', ' I', ' I ', 'I \n', '  I ', 'I  \n', '   I   ']
        replace = ['  ', '  ', '  ', ' \n', '  ', '   ', '  \n', '    ', '   \n', '       ']
        order = [7, 8, 9, 10, 4, 5, 6, 2, 3, 1]
        return ''.join([replace[x] if order[x] in empty else raw[x] for x in xrange(10)])
    
    pins = "{7} {8} {9} {10}\n" + \
    def bowling_pins(arr):
        return pins.format(*(" " if i in arr else "I" for i in range(11)))
    # tipus hibák:
    4: for n in range(7): #lehagyom a ":"-t
    5: zárójel a printnél 
    # egyéb
    6: try-except #blokk
    7: types lekezelése  if isinstance(value, list): vagy if type(value) is list:


Ma Tanultam:
180302:
    return mindenképpen megáll a for ciklusban az első elemnél, nem kell break utána

180301:
    #==, is, trueness
    elif valami == True: helyett is True vagy simán az elif valami is elég, mert az azt nézi hogy true-e

    #clean input
    def check(prompt):
    while True:
        answer= input(prompt).strip().lower()
        if answer in ('yes', 'no'):
            return answer    

180226:
    # chr(i) és ord(i)
    sum(ord(c)-96 for betu in string) #kiszámolja egy stringben az abc betű szerinti számértékét, mintha ezt irnád: 
    for betu in string:
    summ = summ + '_abcdefghijklmnopqrstuvwxyz'.index(betu)

    # __name == __main__  https://www.youtube.com/watch?v=sugvnHA7ElY&
    ha direkt fut, fusson le ami ez alatt van, ha nem csak az fusson le belőle, ami ezen kivül van, vagy amit meghivsz 
    pl az importban, úgy hogy masodik_fajl.main (ha a masodik_fajl.py-t importáltad és abban van def main függvény)

    # dict comprehension  
    trans = {}
    for n, char in enumerate(string.ascii_lowercase): 
    trans[char] = n+1

180225:
    #generátor vs list comprehension 
    gen = (i for i in range(500)) # generátor, nincs listaként belerakva a memóriába
    gen = [i for i in range(500)] # memóriába listaként létre van hozva!!!!

180222:
    #good vs evil kata: a több jegyű stringnél, nem lehet steppel kihagyni a fölösleges karaktereket
    # tehát ez nem jó megoldás:
    for elem in evil[::2]: ha az evil = '10 10 10 10 10 10'

    #zip a megoldás, amikor össze kell szorozni 2 azonos elemszámú stringet, amik végülis numok:
    points_good = [1, 2, 3, 3, 4, 10] ___és___ '10 10 10 10 10 10'
    good = sum([int(x)*y for x, y in zip(good.split(), points_good)]) 
    

180221: 
    # ha vissza akarsz számolni, akkor az első számból a nullára a helyes sorrend
    list[5:0:-1]

    # list comprehension color coded:
    doubled_odds = []
    for n in numbers:
        #if n % 2 == 1:
            doubled_odds.append("n * 2")
    
    doubled_odds = ["n * 2" for n in numbers #if n % 2 == 1]

180221:
     return s.translate(s.maketrans('','',"0123456789"))

180220:
    #file műveletek:
    f.tell -> hol van a "fej"
    f.seek(0) -> ugorjon a ()-dik karakterhez
    f.read(10) - el lehet pl. 10 karaktert beolvasni
    a while ciklusba rakva lehet X karakterenként végig olvasni pl:
        while len(f_contents) > 0: #amig el nem fogy a beolvasandó chunk, addig olvas
            print/append (f_contents, end='*') # * a size_to_read-es chunkokat mutatja
            f_contents = f.read(size_to_read) #beolvassa a következő adagot

180217:
    #még nem értem, de fontos! printen belül 2d listból dolgozó funkció hivás
    for poszt in ["kozeppalyas", "csatar", "hatved"]:
        print("ennyi:", poszt, számoló(focisták,poszt))

    #hogy ne dobja, hogy append() takes exactly one argument (2 given) use []
    vissza.append([elem[0],elem[1]]) #igy lehet két elemet megadni!!!!

180216:

    #egy szövegfájl első "oszlopának" kiprintelése
    for sor in fájl:
        print(sor.split()[0], ", ", sep="" , end="")

    # \ sortörés, hosszú pl if feltételek leirásánál, vagy egy listánál
    lista = ["egy", "kettő", "hárm", \
            "négy", "öt"]

    #nested for olvasása pl  
    sor = 5
    oszlop = 6
    for s in range(sor): #sor 
        for o in range(oszlop): #oszlop
            print("o ", end="")
        print("")
    
    # 4 egymás meleltti 6x3-as mező két sorban ( oooooo oooooo oooooo oooooo)
    szél = 6
    magasság = 3
    mellett = 4
    sor = 2

    for n in range(sor):
        for m in range(magasság):
            for _ in range(mellett):
                print(" ", end="")
                for _ in range(szél):
                    print("o", end="")
            print("")
        print("")


    # Szlávi Péter, Zsakó László nevezék tana 

    #iterable képzés
    #Először a len() függvénnyel meghatározzuk a bejárható \
    # objektum elemszámát, majd ezt betoljuk a range() függvénybe

180215:
    #set = halmaz

    # kirás, olvasás v2
    def kiiras(lista,hova)
    if hova == "sys.stdout": 
        print('\n'.join(lista))
    else:
        céljájl = open(hova, "w")
        print('\n'.join(lista), file=célfájl)
        céljájl.close()

    lista = []
    forrásfájl = open('temp.txt')
    for sor in forrásfájl:
        lista.append(sor.strip())
    forrásfájl.close()

    kiiras(reversed(lista), 'sys.stdout') 


    #betű csere stringben, ha a translat nem működik
        for i in '1234567890':
        s = s.replace(i, '')

180214:
    #Bejáró = iterator 8vagy ciklus változó 
    #bejárandó objektum = iterable 
    #ciklusmag ???

180213:
    #globals = GLOBALS, dictionary-vel lehet 

    #eljárás = nincs visszatérési értéke 
    #függvény (function) = van visszatérési értéke 

    #file beolvasás 
    work_list = []
    inv_file = open("todo.txt","r")
    for sor in inv_file:
        stripped = sor.strip()
        work_list.append(stripped)

    print(work_list)
    inv_file.close()

    #betűnként 
    while True:
    betű = inv_file.read(1)
    if betű:
        print(betű, end='', flush=True)
        time.sleep(.1)
    else:
        break 

    #terminál parancs linuxon
    cat 4.txt (type 4.txt windows-on)

    #check type pl
    type(x) == int 

    #lambda
    y = lambda x: x*2 # mx = lambda x,y: x if  x > y  else y 
    print(y(55))

180212:
    #ha van két külön, de azonos elemszánú lista/tuple, akkor zippel igy lehet belőlük dictinoary-t csinálni:
    dic = dict(zip(month,days))

    #comprehension:
    if v <= 0:         } 
        return 0       | ---->     return 400/v if v > 0 else 0
    else:              | 
        return 400/v   }

180207:
    "nagyitás projekt"
    # ahhoz, hogy ne stringnek printelje ki az alábbi tartalmat:
    board[0][0] = '\033[0;37;41m   |\033[0m'
    # joinolni kellett a cella elemeket és megfelelő [] tömbbé alakitani, 
    # (mert különben több elemnek nézi a join és azt nem fogadja el):
    board2="".join([board[0][0]*2, board[0][1]*2, board[1][0]*2, board[1][1]*2])

    "torpedó"
    board_ai_ships = [0, 0, 0, 0, 0, 0] #ez 5 pozició és 5 érték! nem 5 nulla!

180206:
    # az in-nek kell megnézni, hogy egy string/int benne van-e egy listában, nem az egyenlővel!
    if user_input in allowed_chars:
