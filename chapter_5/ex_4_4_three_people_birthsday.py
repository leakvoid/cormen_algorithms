
# how many people in the room before 3 or more people have the same birthday

import math
import random

def expected_value_2_birthday(k):
    return k * (k - 1) / (2 * 365)

def find_3_birthday_threshold(th):
    res_2 = 1.0
    res_3 = 1.0
    for i in range(2, 365):
        #res_2 *= 1.0 - i / 365
        #res_3 *= 1.0 - (1.0 - res_2) * (math.log(i) / 365) # incorrect estimation
        
        res_3 *= 1.0 - expected_value_2_birthday(i) / 365
        if res_3 < (1 - th):
            return i

def test(c):
    n = find_3_birthday_threshold(c)
    print("Three people have same brithday with", c * 100,"% chance when", n, "in the room")
    
    three_birthday_counter = 0

    for i in range(1000):
        birthdays = set()
        two_birthdays = set()
        for j in range(n):
            new_birthday = random.randint(1, 365)
            if new_birthday in two_birthdays:
                three_birthday_counter += 1
                break
            if new_birthday in birthdays:
                two_birthdays.add(new_birthday)
            else:
                birthdays.add(new_birthday)

    print("For", n, "people in 1000 simulations, 3 birthday cases happened", three_birthday_counter, "times")

for i in range(1,9):
    test(i/10)

