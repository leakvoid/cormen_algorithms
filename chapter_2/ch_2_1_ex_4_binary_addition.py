# BINARY ADDITION

def binary_addition(num_arr_1, num_arr_2):
    if len(num_arr_1) != len(num_arr_2):
        raise Exception('Unequal number of bits')

    n1 = num_arr_1[::-1]
    n2 = num_arr_2[::-1]

    res = [0] * (len(num_arr_1) + 1)
    for i in range(0, len(num_arr_1)):
        if (n1[i] + n2[i] + res[i]) == 3:
            res[i] = 1
            res[i + 1] = 1
        elif (n1[i] + n2[i] + res[i]) == 2:
            res[i] = 0
            res[i + 1] = 1
        elif (n1[i] + n2[i] + res[i]) == 1:
            res[i] = 1
        else:
            res[i] = 0

    return res[::-1]

n1 = [1, 1, 1, 1, 0, 0, 0, 0]
n2 = [1, 1, 0, 0, 1, 1, 0, 0]

print("n1:     " + str(n1))
print("n2:     " + str(n2))

print("sum: " + str(binary_addition(n1, n2)) )
