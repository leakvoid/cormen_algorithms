
# get random(a, b) from random(0, 1)

import math
import random

def random_tree(a, b):
    c = b - a
    p = int(math.ceil(math.log2(c)))
    u_bound = int(math.pow( 2, p ))

    res = -1
    while(res == -1 or res > c):
        res = random_rec(p - 1)
        if(res > c):
            print("out of range", a + res, "repeat")

    return a + res

def random_rec(p):
    if p <= 0:
        return random.randint(0,1)
    else:
        cur = random.randint(0,1) * int(math.pow( 2, p ))
        prev = random_rec(p - 1)
        return cur + prev

for i in range(10):
    print("random(100, 400): ", random_tree(100, 400))
