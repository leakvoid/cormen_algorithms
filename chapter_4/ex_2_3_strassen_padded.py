
# Strassen for non-n^2 cases

from ex_2_2_strassen import square_matrix_multiply
import numpy as np

def pow_zero_pad(A):
    n = len(A)
    m = np.power( 2, np.ceil(np.log2(n)) ).astype(int)
    pad = m - n
    print("n: %s m: %s pad: %s" % (n, m, pad))
    return np.pad(A, [(0, pad), (0, pad)], mode='constant', constant_values=0)

def square_matrix_multiply_padded(A, B):
    n = len(A)
    A = pow_zero_pad(A)
    B = pow_zero_pad(B)
    C = square_matrix_multiply(A, B)
    return C[0:n, 0:n]

# 5 by 5
A = np.array([[10, 20, 30, 40, 50], [11, 21, 31, 41, 51], [12, 22, 32, 42, 52], [13, 23, 33, 43, 53], [14, 24, 34, 44, 54]])
B = np.array([[100, 200, 300, 400, 500], [110, 210, 310, 410, 510], [120, 220, 320, 420, 520], [130, 230, 330, 430, 530], [140, 240, 340, 440, 540]])
C = square_matrix_multiply_padded(A, B)
print("Strassen padded result: ", C)
print("Test: ", np.dot(A, B))
