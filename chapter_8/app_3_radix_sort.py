
# radix sort

def digit_counting_sort(A, d):
    C = [0] * 10

    for j in range(0, len(A[0])):
        C[A[d][j]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    B = []
    for i in range(len(A)):
        B.append([0] * len(A[0]))
    for j in range(len(A[0]) - 1, -1, -1):
        idx = C[A[d][j]] - 1
        for i in range(len(A)):
            B[i][idx] = A[i][j]
        C[A[d][j]] -= 1
    return B


def radix_sort(A, d):
    for i in range(d - 1, -1, -1):
        A = digit_counting_sort(A, i)
    return A

def split_int(A, d):
    res = []
    for i in range(d):
        res.append([])
        
    for j in range(len(A)):
        num = [int(x) for x in str(A[j])]
        for i in range(d):
            res[i].append(num[i])
    return res

def combine_int(A):
    res = []
    for i in range(len(A[0])):
        num = ''
        for j in range(len(A)):
            num += str(A[j][i])
        res.append(int(num))
        
    return res


A = [329, 457, 657, 839, 436, 720, 355]
print("A:", A)
split_A = split_int(A, 3)
print("split:", split_A)
res = radix_sort(split_A, 3)
print("radix_sort:", combine_int(res))

