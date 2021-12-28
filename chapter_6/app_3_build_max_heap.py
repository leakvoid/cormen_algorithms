
# convert array A into max heap

import app_2_max_heapify as mh

import math

def build_max_heap(A):
    A.heap_size = A.length
    for i in range(math.ceil(A.length / 2), -1, -1):
        A = mh.max_heapify(A, i)
    return A

# A = mh.Heap([0, 17, 3, 16, 13, 8, 10, 1, 7, 12, 4, 27, 9, 5])
# print("initial heap:", A)
# A = build_max_heap(A)
# print("max heap:", A)

# A = mh.Heap([5, 3, 17, 10, 84, 19, 6, 22, 9])
# print("ex_3_1: initial heap:", A)
# A = build_max_heap(A)
# print("ex_3_1: max heap:", A)
