
# hash table done via division method

def hash_add(H, key, val):
    h_i = key % 701
    if type(H[h_i]) is str:
        H[h_i] = [] # simple list instead of linked list
    H[h_i].append( (key, val) )

def hash_print(H):
    for i in range(len(H)):
        if type(H[i]) is list:
            for j in range(len(H[i])):
                print("hash:", i, "pair:", H[i][j])

H = [''] * 701
hash_add(H, 22, 'g')
hash_add(H, 723, 'gg')
hash_add(H, 501, 'e')
hash_add(H, 250, 'c')
hash_add(H, 40, 'a')
hash_add(H, 300, 'b')
hash_add(H, 1001, 'bb')
hash_add(H, 502, 'f')
hash_add(H, 0, 't')
hash_add(H, 701, 'tt')

hash_print(H)
