allowed_chars = ("a1", "a2", "a3", "a4", "a5",
                 "b1", "b2", "b3", "b4", "b5",
                 "c1", "c2", "c3", "c4", "c5",
                 "d1", "d2", "d3", "d4", "d5",
                 "e1", "e2", "e3", "e4", "e5",
                 "f1", "f2", "f3", "f4", "f5",
                 )

print(allowed_chars)
hits = []
user_input = ()
while True:
    user_input = input("target?").lower()  # loweresitjük, hogy ne kelljen annyi félét nézni
    if user_input in hits:
        print("már volt")
    elif user_input in allowed_chars:
        print("ok")
        hits.append(user_input)
        break
    else:  # ez miért nem fut le?
        print("wrong format")
