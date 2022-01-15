
# randomized select procedure for finding i-th lowest element

import os
import sys
sys.path.append(os.getcwd()[:-1] + '7')
import app_1_quicksort as qs

import random

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A_tmp = A[i]
    A[i] = A[r]
    A[r] = A_tmp
    return qs.partition(A, p, r)

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print("A before:", A)
print("select 3-d lowest element:", randomized_select(A, 0, len(A) - 1, 3))
print("select lowest element:", randomized_select(A, 0, len(A) - 1, 1))
print("select 5-th lowest element:", randomized_select(A, 0, len(A) - 1, 5))
print("A after:", A)
