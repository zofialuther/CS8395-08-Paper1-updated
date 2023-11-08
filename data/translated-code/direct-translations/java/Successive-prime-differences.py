```python
def sieve(limit):
    primes = [2]
    c = [False] * (limit + 1)  # composite = True
    p = 3
    while True:
        p2 = p * p
        if p2 > limit:
            break
        for i in range(p2, limit + 1, 2 * p):
            c[i] = True
        while c[p]:
            p += 2
    for i in range(3, limit + 1, 2):
        if not c[i]:
            primes.append(i)
    return primes


def successive_primes(primes, diffs):
    results = []
    dl = len(diffs)
    for i in range(len(primes) - dl):
        group = [None] * (dl + 1)
        group[0] = primes[i]
        for j in range(i, i + dl):
            if primes[j + 1] - primes[j] != diffs[j - i]:
                break
            group[j - i + 1] = primes[j + 1]
        else:
            results.append(group)
    return results


primes = sieve(999999)
diffs_list = [[2], [1], [2, 2], [2, 4], [4, 2], [6, 4, 2]]
print("For primes less than 1,000,000:-\n")
for diffs in diffs_list:
    print(f"  For differences of {diffs} ->")
    sp = successive_primes(primes, diffs)
    if not sp:
        print("    No groups found")
        continue
    print(f"    First group   = {sp[0]}")
    print(f"    Last group    = {sp[-1]}")
    print(f"    Number found  = {len(sp)}\n")
```