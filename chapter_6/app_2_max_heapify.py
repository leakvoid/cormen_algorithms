
# max heapify for maintaining max heap property at i

import math

class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr)
        self.length = len(arr)

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __str__(self):
        res = "\n"
        last_height = 0
        n = len(self.arr)
        max_n = math.pow(2, math.ceil(math.log2(n + 1)))
        spacing = int(max_n / 2) - 1
        for i in range(n):
            current_height = math.floor(math.log2(i + 1))
            if last_height != current_height:
                last_height = current_height
                spacing = int(math.ceil(max_n / math.pow(2, last_height + 1)))
                res += "\n"
                
            res += " " * spacing + str(self.arr[i]) 
        return res
        #return str(self.arr)

    def append(self, value):
        if self.length > self.heap_size:
            last = self.heap_size - 1
            self.arr[last] = value
        else:
            self.arr.append(value)
        self.length += 1
        

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i):
    largest = 0
    l = left(i)
    r = right(i)
    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        print("Swap", A[i], "with", A[largest])
        A_tmp = A[i]
        A[i] = A[largest]
        A[largest] = A_tmp
        return max_heapify(A, largest)
    return A

# A = Heap([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
# print("initial heap:", A)
# print("heap after max_heapify:", max_heapify(A, 2))
