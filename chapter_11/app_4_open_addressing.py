
m = 10

# double hasing method
def compute_hash(k, i):
    h1 = k % m
    h2 = 1 + k % (m - 1)
    return (h1 + i * h2) % m

def hash_insert(T, k):
    i = 0
    while True:
        j = compute_hash(k, i)
        if T[j] == '':
            T[j] = k
            return j
        else:
            i += 1

        if i == m:
            break
    raise Exception("hash table overflow")

def hash_search(T, k):
    i = 0
    while True:
        j = compute_hash(k, i)
        if T[j] == k:
            return j
        i += 1

        if i == m or T[j] == '':
            break

    return None

def hash_print(H):
    for i in range(m):
        if H[i] != '':
            print("hash:", i, "key:", H[i])

H = [''] * (m + 1)
hash_insert(H, 22)
hash_insert(H, 723)
hash_insert(H, 501)
hash_insert(H, 250)
hash_insert(H, 40)
hash_insert(H, 300)
hash_insert(H, 1001)
hash_insert(H, 1001)
hash_insert(H, 1001)
hash_insert(H, 1001)

hash_print(H)
