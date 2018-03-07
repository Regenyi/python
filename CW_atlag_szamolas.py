# Benefactor feladat Python2

def new_avg(arr, newavg):
    if arr == []:
        arr = [1]
#    c = (newavg - (sum(arr))/(len(arr)+1)) * (len(arr)+1)
    c = (newavg - (sum(arr)/(len(arr)+1))) * (len(arr)+1)
    print(newavg*float(len(arr) + 1) - sum(arr))
    if c > 0:
        return round(c)
    else:
        return -1 

lista = [14, 30, 5, 7, 9, 11, 15]
new_avg(lista,90)





