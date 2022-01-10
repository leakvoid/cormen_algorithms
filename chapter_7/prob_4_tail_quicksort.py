
# tail recursive quicksort

import app_1_quicksort as qs

def tail_recursive_quicksort(A, p, r):
    while p < r:
        print("p:", p, "r:", r)
        q = qs.partition(A, p, r)
        print("q:", q)
        tail_recursive_quicksort(A, p, q - 1)
        #quicksort(A, q + 1, r)
        p = q + 1

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print("initial array:", A)
tail_recursive_quicksort(A, 0, len(A) - 1)
print("tail recursive quicksort:", A)
