from itertools import accumulate

def repString(n, s):
    return ''.join([x for d, x in zip(accumulate([n], lambda x, _: x//2), (s*2 for _ in range(n))) if d > 0])

# TEST
print(repString(500, "ha"))