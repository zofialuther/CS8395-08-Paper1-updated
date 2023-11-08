from itertools import combinations

def disjoint(a):
    result = []
    for n in range(1, len(a) - 1):
        left = a[:n]
        right = a[n:]
        for b in combinations(right, len(right)):
            for a in (left[i:] for i in range(len(left))):
                result.append(list(a) + list(b))
    return result

print(len(disjoint(list(range(1, 21)))))