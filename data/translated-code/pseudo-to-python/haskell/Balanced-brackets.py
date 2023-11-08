import random

def pairs(l, u, r):
    result = []
    i = l
    while i < u:
        j = random.randint(i, u)
        result.append([i, j])
        i += 1
    return result

def shuffle(xs, r):
    v = xs.copy()
    pairs_list = pairs(0, len(v) - 1, r)
    for pair in pairs_list:
        v[pair[0]], v[pair[1]] = v[pair[1]], v[pair[0]]
    return v