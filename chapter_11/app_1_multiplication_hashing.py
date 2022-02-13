
# hash table done via multiplication method

import math

p = 14
m = 2 ** p
A = ( math.sqrt(5) - 1 ) / 2
w = 32
s = math.floor(A * 2 ** w)

def msb(n, p):
    b = bin(n)
    return int(b[0:int(2 + p)], 2) # book error

def hash_add(H, key, val):
    r0 = (key * s) % (2 ** w)
    #print(r0)
    h_i = msb(r0, p)
    if type(H[h_i]) is str:
        H[h_i] = []
    H[h_i].append( (key, val) )

def hash_print(H):
    for i in range(len(H)):
        if type(H[i]) is list:
            for j in range(len(H[i])):
                print("hash:", i, "pair:", H[i][j])        

H = [''] * m
hash_add(H, 123456, 'v')
hash_add(H, 1, 'a')
hash_add(H, 12, 'b')
hash_add(H, 123, 'c')
hash_add(H, 1234, 'd')
hash_add(H, 12345, 'e')
hash_add(H, 0, 'f')
hash_add(H, 33, 'g')
hash_add(H, 544, 'h')

hash_print(H)
