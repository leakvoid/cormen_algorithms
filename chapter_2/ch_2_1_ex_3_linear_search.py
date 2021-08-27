# LINEAR SEARCH

def linear_search(arr, val):
    for i in range(0, len(arr)):
        if val == arr[i]:
            return i

    return -1

A = [5, 2, 4, 6, 1, 3]
print("Initial array: " + str(A))

v = 6
index = linear_search(A, v);
print("Position for " + str(v) + " in array is " + str(index))

v = 10
index = linear_search(A, v);
print("Position for " + str(v) + " in array is " + str(index))
