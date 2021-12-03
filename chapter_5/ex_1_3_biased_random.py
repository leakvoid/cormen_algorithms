
# get 50/50 random function from unknown biased random

import math
import random

# bias_rate = 1 - no bias; x - x times more likely
def biased_random(bias_rate):
    res = random.randint(0, bias_rate)
    if res == 0:
        return 0
    else:
        return 1

def repeat_until_ones(bias_rate):
    zero_c = 0
    one_c = 0

    while zero_c == 0 or one_c == 0:
        res = biased_random(bias_rate)
        if res == 0:
            zero_c += 1
        else:
            one_c += 1

    return zero_c + one_c
        
def unbiased_random(bias_rate):
    reps_first = repeat_until_ones(bias_rate)
    reps_second = repeat_until_ones(bias_rate)

    if reps_first > reps_second:
        return 0
    elif reps_first < reps_second:
        return 1
    else:
        return unbiased_random(bias_rate)

def test(bias_rate):
    print("testing debiasing with", bias_rate ,"to 1 bias")
    zero_c = 0
    one_c = 0
    for i in range(1000):
        res = unbiased_random(bias_rate)
        if res == 0:
            zero_c += 1
        else:
            one_c += 1

    print("distribution after 1000 iterations:", zero_c, "/", one_c)

test(9)
test(3)
test(1)
            

#for i in range(20):
#    print("biased_random(10): ", biased_random(10))
