#Merge sort algo by 'ZR_huang'
#Note: this code is not written by me
def Merge(A,B):
    i = 0
    j = 0
    result = []

    for k in range(len(A)+len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            elif B[j] < A[i]:
                result.append(B[j])
                j += 1
            else:
                result.append(A[i])
                result.append(B[j])
                i += 1
                j += 1
        elif i == len(A):
            result.append(B[j])
            j += 1
        elif j == len(B):
            result.append(A[i])
            i += 1
    
    return result

def Sort(array):
    if len(array) == 1:
        return array
  
    left = array[:int(len(array)/2)]
    right = array[int(len(array)/2):]
    
    result_left = Sort(left)
    result_right = Sort(right)
    
    result = Merge(result_left,result_right)

    return result


array = []
with open(r"C:\Users\DIVYALOK\Downloads\Algo_Assign_Material\Assignment2.txt", "r+") as f:
    for line in f.readlines():
        array.append(int(line.strip()))

print(Sort(array))

#r"C:\Users\DIVYALOK\Downloads\Algo_Assign_Material\Assignment2.txt", "r+"