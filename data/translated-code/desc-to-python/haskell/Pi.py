def g(a, b, c, d, e, f):
    result = [a, b, c]
    for i in range(3, 10):
        next_num = d * result[i-1] - e * result[i-2] + f * result[i-3]
        result.append(next_num)
    return result

def pi_():
    return g(1, 0, 1, 1, 3, 3)