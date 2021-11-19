
# SQUARE MATRIX MULTIPLICATION

import numpy as np

def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise Exception("Error: Matrix multiplication shape mismatch")

    C = np.zeros((A.shape[0], B.shape[1]), dtype=int)

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[10, 20], [30, 40], [50, 60]])
print("custom: ", matrix_multiply(A, B))
print("np.dot: ", np.dot(A, B))
