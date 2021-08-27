# INSERTION SORT ALGORITHM

def pred(a, b, order = 'desc'):
    return (a < b) if (order == 'desc') else (a > b)

def insertion_sort(A, order = 'desc', verbose = True):
    for i in range(1, len(A)):
        key = A[i]
        
        j = i - 1
        while j >= 0 and pred(A[j], key, order):
            A[j + 1] = A[j]
            j -= 1
            if verbose:
                print("Inner loop array: " + str(A))

        A[j + 1] = key
        if verbose:
            print("Inserting at A[" + str(j + 1) + "] key " +
                  str(key) + " resulting array: " + str(A))


arr = [5, 2, 4, 6, 1, 3]
print("Initial array: " + str(arr))

insertion_sort(arr);
print("Insertion sort desc result: " + str(arr))

insertion_sort(arr, 'asc');
print("Insertion sort asc result: " + str(arr))

