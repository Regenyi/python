import time
start = time.time()
#16785407

tesztelendő = 16785407 #int(input("mi a szám? "))

for i in range(3, int(tesztelendő/2), 2): # 1.123319149017334 idő alatt fut le 
    if tesztelendő % i == 0: 
        print(i)
        print("ez nem prima")
        break
else:
    print("ez primszám!")

end = time.time()
print(end - start)
