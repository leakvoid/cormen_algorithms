
# get uniform random permutation by sorting

import math
import random

def permute_by_sorting(A):
    n = len(A)
    P = [-1] * n
    
    for i in range(n):
        # avoiding duplicates can be more efficient, but it's not the focus here
        while True: 
            P_tmp = random.randint(0, math.pow(n, 3))
            if P_tmp not in P:
                P[i] = P_tmp
                break

    A_perm = [0] * n
    P_sorted = sorted(P)
    for i in range(n):
        A_perm[i] = A[P.index(P_sorted[i])]

    return A_perm

A = ["C", "Z", "A", "K", "Y", "L"]
for i in range(10):
    print("permutation: ", permute_by_sorting(A))
        
