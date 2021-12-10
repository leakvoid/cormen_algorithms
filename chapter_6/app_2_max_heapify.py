
# max heapify for maintaining max heap property at i

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(A, i):
    largest = -1
    l = left(i)
    r = right(i)
    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        print("Swap", A[i], "with", A[largest])
        A_tmp = A[i]
        A[i] = A[largest]
        A[largest] = A_tmp
        return max_heapify(A, largest)
    return A

A = [0, 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
print("initial array:", A)
print("result array:", max_heapify(A, 3))
