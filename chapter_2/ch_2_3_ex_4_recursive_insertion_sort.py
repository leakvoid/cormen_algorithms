# RECURSIVE INSERTION SORT

def insertion_sort(A):
    insertion_sort_rec(A, len(A) - 1)

def insertion_sort_rec(A, p):
    if p > 0:
        insertion_sort_rec(A, p - 1)
        insert(A, p)

def insert(A, p):
    key = A[p]

    i = p - 1
    while i >= 0 and A[i] < key:
        A[i + 1] = A[i]
        i -= 1

    A[i + 1] = key


arr = [5, 2, 4, 6, 1, 3]
print("Initial array: " + str(arr))

insertion_sort(arr);
print("Recursive insertion sort result: " + str(arr))
