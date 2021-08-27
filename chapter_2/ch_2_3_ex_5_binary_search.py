# BINARY SEARCH

import math

def binary_search(A, s_param):
    return binary_search_rec(A, s_param, 0, len(A) - 1)

def binary_search_rec(A, s_param, start, end):
    if start > end:
        return -1
    
    mid = math.floor( (end + start) / 2 )
    print("start: " + str(start) + " mid: " + str(mid) + " end: " + str(end))

    if A[mid] == s_param:
        return mid
    elif A[mid] > s_param:
        return binary_search_rec(A, s_param, start, mid - 1)
    elif A[mid] < s_param:
        return binary_search_rec(A, s_param, mid + 1, end)

import random

arr = []
for i in range(10):
    arr.append( random.randrange(100) )

arr = sorted(arr)
print("Initial array: " + str(arr))

s_param = arr[random.randrange(10)]
idx = binary_search(arr, s_param)
print("Paramether " + str(s_param) + " found at position " + str(idx))

s_param = 150
idx = binary_search(arr, s_param)
print("Paramether " + str(s_param) + " not found. Result " + str(idx))
