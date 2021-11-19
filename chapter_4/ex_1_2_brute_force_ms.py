
# BRUTE FORCE MAXIMUM SUBARRAY Theta(n^2)

import math

def brute_force(A):
    max_gain = 0
    max_buy = 0
    max_sell = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            gain = A[j] - A[i]
            if(gain > max_gain):
                max_gain = gain
                max_buy = i
                max_sell = j

    return (max_gain, max_buy, max_sell)

A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print("Array: ", A)

(max_gain, i, j) = brute_force(A)
print("Brute force: [", A[i], ",", A[j], "]")
