def elimination(arr):
    # megnézem az array-ben egyesével, hogy volt-e már az elem
    #count, set
    #bejárom az array-t, és az első elem értékét összehasonlitom a kövtekző\
    #  elem értékéhez és ha azonos, akkor returnölöm, ha else, akkor none-t adok vissza. 
    for i in range(len(arr)-1):
        print(i,arr[i])
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                print(arr[i])


elimination([2, 1, 5, 34, 1, 22, 1])