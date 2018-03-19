#def elimination(arr):
    # megnézem az array-ben egyesével, hogy volt-e már az elem
    #count, set
    #bejárom az array-t, és az első elem értékét összehasonlitom a kövtekző\
    #  elem értékéhez és ha azonos, akkor returnölöm, ha else, akkor none-t adok vissza. 
    # for i in range(len(arr)-1):
    #     #print(i,arr[i])
    #     for j in range(len(arr)-1):
    #         if arr[i] == arr[j+1]:
    #             print(arr[i])
    #             return arr[i]
    #             break
    #         break
    #     else:
    #         return None


# Python code t get difference of two lists
# Not using set()
def Diff(li1, li2):
    li_dif = [i for i in li2 if i in li1]
    print(li_dif)
    return li_dif
    

# Driver Code
arr = [2, 1, 5, 34, 1, 22, 1]
li1 = arr
li2 = list(set(arr))
li3 = Diff(li1, li2)
print(li1, li2)

def elimination2(arr):
    s = set(arr)
    print(s)
    #temp3 = [x for x in arr if x not in s]
    temp3=list(set(temp1) - set(arr))
    print(temp3)

#elimination2([2, 1, 5, 34, 1, 22, 1])
 
