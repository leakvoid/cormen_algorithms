# HORNER RULE

def calc_normal(A, x):
    y = 0
    for i in range(len(A)):
        y += A[i] * math.pow(x, i)
    return y

def calc_horner(A, x):
    #for i, e in reversed(list(enumerate(A))):
    y = 0
    for i in range(len(A) - 1, -1, -1):
        y = A[i] + x * y
    return y

def calc_horner_rec(A, x, i = 0):
    if i < len(A) - 1:
        print("A[" + str(i) + "] + x * (", end = '')
        res = A[i] + x * calc_horner_rec(A, x, i + 1)
        print(")", end = ('\n' if i == 0 else ''))
        return res
    else:
        print("A[" + str(i) + "]", end = '')
        return A[i]

import math

A = [4.0, 3.0, 0.0, 5.0]
x = 11.0

print("Normal: ", calc_normal(A, x))
print("Horner: ", calc_horner(A, x))
res = calc_horner_rec(A, x)
print("Horner(rec): ", res)

