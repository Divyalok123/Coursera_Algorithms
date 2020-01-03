#Merge sort algo written by 'Divyalok'
def mergesort(arr):
    n = len(arr)
    if(n < 2):
        return arr
    mid = n // 2
    left = [None]*mid
    right = [None]*(n - mid)
    for i in range(0, mid):
        left[i] = arr[i]
    for i in range(mid, n):
        right[i-mid] = arr[i]
    r_left = mergesort(left)
    r_right = mergesort(right)
    inverse_count = merge(r_left, r_right, arr)
    return inverse_count

def merge(left, right, arr):
    n_left = len(left)
    n_right = len(right)
    i = 0
    j = 0
    k = 0
    inverse_count = 0
    while(i < n_left and j < n_right):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            inverse_count += int(n_left-i) + 1
            j += 1
        k += 1
    
    while(i < n_left):
        arr[k] = left[i]
        i += 1
        k += 1
    while(j < n_right):
        arr[k] = right[j]
        j += 1
        k += 1
    return inverse_count

readfile = open(
    r"C:\Users\DIVYALOK\Downloads\Algo_Assign_Material\Assignment2.txt", "r+"
)
readlines = readfile.readlines()
array = [line.replace("\n", "") for line in readlines]

value = mergesort(array)
print(value)

#This code is giving TypeError: object of type 'int' has no len(), line 20, "n_right = len(right)"