
# bucket sort for uniformally distributed [0, 1) ranges

import math

def bucket_sort(A):
    n = len(A)
    B = []
    for i in range(n - 1):
        B.append([]) # linked list is optional

    for i in range(n):
        B[ math.floor(n * A[i]) ].append(A[i])

    print("B intermidiate:", B)

    res = []
    for i in range(n - 1):
        B[i].sort() # insertion sort is more accurate
        res += B[i]

    return res

A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
print("A:", A)
print("bucket sort:", bucket_sort(A))
