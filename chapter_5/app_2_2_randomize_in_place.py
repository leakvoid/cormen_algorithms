
# get uniform random permutation by in-place randomization

import random

def randomize_in_place(A):
    n = len(A)
    for i in range(n - 1):
        new_i = random.randint(i, n - 1)
        A_tmp = A[i]
        A[i] = A[new_i]
        A[new_i] = A_tmp

    return A

A = ["C", "Z", "A", "K", "Y", "L"]
for i in range(10):
    print("permutation: ", randomize_in_place(A))

