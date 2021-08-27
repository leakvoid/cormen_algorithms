# SELECTION SORT

def selection_sort(arr, order = 'desc'):
    for i in range(0, len(arr) - 1):
        ext_i = i
        for j in range(i + 1, len(arr)):
            if (order == 'desc' and arr[ext_i] < arr[j]) or \
               (order == 'asc' and arr[ext_i] > arr[j]):
                ext_i = j
        tmp = arr[i]
        arr[i] = arr[ext_i]
        arr[ext_i] = tmp
                
arr = [5, 2, 4, 6, 1, 3]
print("Initial array: " + str(arr))

selection_sort(arr);
print("Insertion sort desc result: " + str(arr))

selection_sort(arr, 'asc');
print("Insertion sort asc result: " + str(arr))
