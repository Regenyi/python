def elimination2(arr):
    for num in arr:
        if arr.count(num) == 2:
            return num

def elimination(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            
            if arr[i] == arr[j]:
                print(arr[i])
                return(arr[i])

elimination([2, 1, 5, 34, 1, 22, 1])