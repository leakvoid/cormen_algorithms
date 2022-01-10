
# quicksort with same elements

def quicksort(A, p, r):
    print("quicksort call:", p, r)
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    #print("partition call:", p, r)
    
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            
            A_tmp = A[i]
            A[i] = A[j]
            A[j] = A_tmp
            
    A_tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = A_tmp
    return i + 1

A = 10 * [7]
print("same element array:", A)
quicksort(A, 0, len(A) - 1)
# Worst case with same element calls
# T(n) = T(n - 1) + c * n
