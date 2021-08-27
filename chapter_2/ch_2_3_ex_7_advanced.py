# TWO-ELEMENT SUM SEARCH

import math

def pair_sum_search(arr, x):
    s_arr = sorted(arr) # n lg n

    res = []
    for i in range(0, len(s_arr)): # n
        x1 = s_arr[i]

        s_val = rec_psum_search(s_arr, x1, x, i + 1, len(s_arr) - 1) # lg n
        if s_val != -1:
            res.append( [s_arr[i], s_arr[s_val]] )

    return res

# alternatively do bin search and pass x2 = x - x1 instead
def rec_psum_search(arr, x1, x, start, end):
    if start > end:
        return -1

    mid = math.floor( (end + start) / 2 )
        
    sum_res = x1 + arr[mid]
    if sum_res == x:
        return mid
    elif sum_res > x:
        return rec_psum_search(arr, x1, x, start, mid - 1)
    else:
        return rec_psum_search(arr, x1, x, mid + 1, end)
    
            

arr = [15, 1, 12, 3, 22, 88, 95, 23, 57, 23, 17, 4, 73, 25]
print("arr: ", arr)

x = 25
print("x: ", x)
print("result: ", pair_sum_search(arr, x))

x = 96
print("x: ", x)
print("result: ", pair_sum_search(arr, x))

x = 337
print("x: ", x)
print("result: ", pair_sum_search(arr, x))
