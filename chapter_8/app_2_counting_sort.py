
# counting sort

def counting_sort(A, k):
    C = [0] * (k + 1)

    for j in range(0, len(A)):
        C[A[j]] += 1
    print("number of elements[C]:", C)

    for i in range(1, len(C)):
        C[i] += C[i - 1]
    print("noe less then or equal to[C]:", C)

    B = [0] * len(A)
    for j in range(len(A) - 1, -1, -1):
        print("j:",j)
        print("A[j]:",A[j])
        print("C[A[j]]:",C[A[j]])
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    return B
        
A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
print("initial array:", A)
B = counting_sort(A, 6)
print("counting sort:", B)
