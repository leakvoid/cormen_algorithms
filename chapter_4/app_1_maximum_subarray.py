# FIND MAXIMUM SUBARRAY

import math

INT_NINF = float('-inf')

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = INT_NINF
    max_left = mid
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = INT_NINF
    max_right = mid + 1
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = math.floor( (low + high) / 2 )
        
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print("Array: ", A)
(low, high, sum) = find_maximum_subarray(A, 0, len(A) - 1)
print("Max subarray: ", A[low:high + 1])

# ex_1_1 all negative
A = [-10, -103, -54, -4, -15, -22]
print("Array: ", A)
(low, high, sum) = find_maximum_subarray(A, 0, len(A) - 1)
print("Max subarray: ", A[low:high + 1])
