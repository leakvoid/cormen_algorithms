
# heapsort algorithm

import app_2_max_heapify as mh
import app_3_build_max_heap as bmh

def heapsort(A):
    A = bmh.build_max_heap(A)
    for i in range(A.length - 1, 1, -1):
        A_tmp = A[i]
        A[i] = A[0]
        A[0] = A_tmp
        A.heap_size = A.heap_size - 1
        A = mh.max_heapify(A, 0)
    return A

A = mh.Heap([5, 13, 2, 25, 7, 17, 20, 8, 4])
print("initial heap:", A)
print("heapsort:", heapsort(A))

A = [1, 2, 3, 4]
def test(A):
    for i in range(len(A) - 1, -1, -1):
        print("A[" + str(i) + "]:", A[i])

test(A)
