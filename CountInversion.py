

#My code for mergesort including the count of inversions which is not returning the correct sorted list
def SortAndCount(arr):
    n = len(arr)
    if(n == 1):
        return arr  
    mid = n // 2
    left = [None]*mid
    right = [None]*(n - mid)
    for i in range(0, mid):
        left[i] = arr[i]
    for i in range(mid, n):
        right[i-mid] = arr[i]
    r_left = SortAndCount(left)
    r_right = SortAndCount(right)
    return mergeAndCount(r_left, r_right, arr)

def mergeAndCount(r_left, r_right, arr):
    n_left = len(r_left)
    n_right = len(r_right)
    i = 0
    j = 0
    k = 0
    inversion_count = 0
    while i < n_left and j < n_right:
        if r_left[i] < r_right[j]:
            arr[k] = r_left[i]
            i += 1
        else:
            arr[k] = r_right[j]
            j += 1
            inversion_count += (n_left-i + 1)
        k += 1
    
    while i < n_left:
        arr[k] = r_left[i]
        i += 1
        k += 1
    while j < n_right:
        arr[k] = r_right[j]
        j += 1
        k += 1
    return inversion_count

readfile = open(
    r"C:\Users\DIVYALOK\Downloads\Algo_Assign_Material\Assignment2.txt", "r+"
)
readlines = readfile.readlines()
array = [line.replace("\n", "") for line in readlines]

result_array = SortAndCount([1, 3, 5, 2, 4, 6])
print(result_array)

#r_array = mergesort([99979, 9998, 99981])
#print(r_array)