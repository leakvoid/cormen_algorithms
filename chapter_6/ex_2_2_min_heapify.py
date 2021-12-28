
# min heapify

import app_2_max_heapify as mh

def min_heapify(A, i):
    smallest = 0
    l = mh.left(i)
    r = mh.right(i)
    if l < A.length and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < A.length and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        print("Swap", A[i], "with", A[smallest])
        A_tmp = A[i]
        A[i] = A[smallest]
        A[smallest] = A_tmp
        return min_heapify(A, smallest)
    return A
    
A = mh.Heap([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
print("initial heap:", A)
print("heap after min_heapify:", min_heapify(A, 0))
