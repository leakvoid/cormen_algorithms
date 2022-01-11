
# how many integers fall within [a..b] range on preprocessed input in O(1) time

# runs in O(n + k)
def preprocess(A, k):
    C = [0] * (k + 1)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    return C

# runs in O(1)
def count_in_range(a, b, C):
    if a > len(C):
        return 0
    if b >= len(C):
        b = len(C) - 1
    if a <= 0:
        return C[b]

    return C[b] - C[a - 1]

A = [2, 4, 2, 3, 3, 7, 5, 1, 2, 8, 3, 8, 0, 9]
print("A:", A)
print("len", len(A))
C = preprocess(A, 9)
print("C:", C)
print("[0,3]:", count_in_range(0, 3, C))
print("[12,15]:", count_in_range(12, 15, C))
print("[5,18]:", count_in_range(5, 18, C))
print("[0,20]:", count_in_range(0, 20, C))
