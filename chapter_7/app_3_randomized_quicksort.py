
# randomized quicksort

import app_1_quicksort as qs
import random

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A_tmp = A[i]
    A[i] = A[r]
    A[r] = A_tmp
    return qs.partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print("initial array:", A)
randomized_quicksort(A, 0, len(A) - 1)
print("randomized quicksort:", A)

