# BUBBLE SORT

def bubble_sort(A):
    for i in range(0, len(A) - 2):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                print("Swap " + str(A[j]) + " with " + str(A[j - 1]))
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp

import random

arr = []
for i in range(10):
    arr.append( random.randrange(100) )
print("Initial array: " + str(arr))

bubble_sort(arr)
print("Bubble sort result: " + str(arr))
