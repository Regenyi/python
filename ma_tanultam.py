Kérdések:
    #ez miért nem csinálja amit csinálnia kellene?
    lista = [66, -45,-12,99,34,-1,5,8,4]
    print(sorted(lista, key=abs, reverse=True)) 

    #ez se megy:
    return s.translate(None, "0123456789")


    

Ma Tanultam:

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
