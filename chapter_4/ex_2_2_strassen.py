
# Strassen matrix multiplication Theta(n ^ lg2(7))

import math
import numpy as np

def square_matrix_multiply(A, B):
    if A.shape[1] != B.shape[0] or A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        raise Exception("Error: Matrix multiplication shape mismatch")
    
    n = A.shape[0]
    h = math.floor( n / 2 )

    if n == 1:
        return A * B

    A11 = A[0:h, 0:h]
    A12 = A[0:h, h:n]
    A21 = A[h:n, 0:h]
    A22 = A[h:n, h:n]
    print("A11: ", A11)
    print("A12: ", A12)
    print("A21: ", A21)
    print("A22: ", A22)

    B11 = B[0:h, 0:h]
    B12 = B[0:h, h:n]
    B21 = B[h:n, 0:h]
    B22 = B[h:n, h:n]
    print("B11: ", B11)
    print("B12: ", B12)
    print("B21: ", B21)
    print("B22: ", B22)

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    P1 = square_matrix_multiply(A11, S1)
    P2 = square_matrix_multiply(S2, B22)
    P3 = square_matrix_multiply(S3, B11)
    P4 = square_matrix_multiply(A22, S4)
    P5 = square_matrix_multiply(S5, S6)
    P6 = square_matrix_multiply(S7, S8)
    P7 = square_matrix_multiply(S9, S10)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    print("C11: ", C11)
    print("C12: ", C12)
    print("C21: ", C21)
    print("C22: ", C22)

    C1 = np.concatenate((C11, C12), axis=1)
    C2 = np.concatenate((C21, C22), axis=1)
    C = np.concatenate((C1, C2), axis=0)
    return C

# 4 by 4
A = np.array([[10, 20, 30, 40], [11, 21, 31, 41], [12, 22, 32, 42], [13, 23, 33, 43]])
B = np.array([[100, 200, 300, 400], [110, 210, 310, 410], [120, 220, 320, 420], [130, 230, 330, 430]])
C = square_matrix_multiply(A, B)
print("Strassen result: ", C)
print("Test: ", np.dot(A, B))
