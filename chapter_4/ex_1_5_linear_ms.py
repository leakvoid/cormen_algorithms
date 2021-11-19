
# LINEAR MAXIMUM SUBARRAY

import math

INT_NINF = float('-inf')

def maximum_subarray_linear(A):
    max_sum = INT_NINF
    max_left = 0
    max_right = 0
    
    current_sum = 0
    current_left = 0

    for i in range(len(A)):
        current_sum += A[i]
        if current_sum > max_sum:
            max_sum = current_sum
            max_left = current_left
            max_right = i
        elif current_sum < 0:
            current_sum = 0
            current_left = i + 1

    return (max_sum, max_left, max_right)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print("Array: ", A)
(max_sum, max_left, max_right) = maximum_subarray_linear(A)
print("Max subarray: ", A[max_left:max_right + 1])
