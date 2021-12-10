
# how many people needed in a room to have 50% of same birthsday

def inverse_sum_upto_one(n):
    sum = 0.0
    for i in range(n, 0, -1):
        sum += 1.0 / i
        if sum >= 1:
            print("Reached one at i = ", i)
            break

inverse_sum_upto_one(1000000)
inverse_sum_upto_one(100000)
inverse_sum_upto_one(10000)
inverse_sum_upto_one(1000)
inverse_sum_upto_one(100)
inverse_sum_upto_one(10)
inverse_sum_upto_one(5)
