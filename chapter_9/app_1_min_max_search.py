
# simultaneous search for minimum and maximum

def min_max_search(A):
    if A[0] < A[1]:
        min = A[0]
        max = A[1]
    else:
        min = A[1]
        max = A[0]

    for i in range(3, len(A), 2):
        if A[i] < A[i - 1]:
            l_min = A[i]
            l_max = A[i - 1]
        else:
            l_min = A[i - 1]
            l_max = A[i]

        if l_min < min:
            min = l_min
        if l_max > max:
            max = l_max

    last = len(A) - 1
    if i < last:
        if A[last] < min:
            min = A[last]
        if A[last] > max:
            max = A[last]
    
    return {"min": min, "max": max}

A = [3, 12, 4, 2, 11, 7, 16, 23, 8, 20]
print("A:", A)
print(min_max_search(A))
A.append(200)
print("updated A:", A)
print(min_max_search(A))
