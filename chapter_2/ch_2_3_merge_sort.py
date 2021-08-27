# MERGE SORT

import math

def merge_sort(arr):
    p = 0
    r = len(arr) - 1
    merge_sort_rec(arr, p, r)

def merge_sort_rec(arr, p, r):
    if p < r:
        print( "A: " + str( arr[p:r + 1] ) + " p: " + str(p) + " r: " + str(r) )
        q = math.floor( (p + r) / 2 )
        merge_sort_rec(arr, p, q)
        merge_sort_rec(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    L = []
    for i in range(0, n1):
        L.append( arr[p + i] )

    R = []
    for j in range(0, n2):
        R.append( arr[q + j + 1] )

    i = 0
    j = 0
    for k in range(p, r + 1):
        if i >= len(L) or j >= len(R):
            break
        
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

    if i < len(L):
        for t in range(k, r + 1):
            arr[t] = L[i]
            i += 1
    elif j < len(R):
        for t in range(k, r + 1):
            arr[t] = R[j]
            j += 1

arr = [3, 41, 52, 26, 38, 57, 9, 49]
merge_sort(arr)

print(str(arr))
