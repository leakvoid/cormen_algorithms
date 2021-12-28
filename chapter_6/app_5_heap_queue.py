
# heap queue implementation

import app_2_max_heapify as mh
import math

def parent(i):
    return int(math.ceil(i / 2) - 1)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    if A.heap_size < 1:
        print("ERROR: heap underflow")
        return

    max = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size = A.heap_size - 1
    mh.max_heapify(A, 0)
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("ERROR: new key is smaller than current key")
        return

    A[i] = key
    print("add element:", A)
    while i > 0 and A[parent(i)] < A[i]:
        # print("i:", i, "parent:", parent(i))
        A_tmp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = A_tmp
        print("swap", A[i], "with", A[parent(i)], A)
        i = parent(i)

def max_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A.append(-math.inf)
    heap_increase_key(A, A.heap_size - 1, key)
    return A

A = mh.Heap([27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])
print("initial heap:", A)
print("after max_heap_insert 15:", max_heap_insert(A, 15))
print("after max_heap_insert 18:", max_heap_insert(A, 18))
