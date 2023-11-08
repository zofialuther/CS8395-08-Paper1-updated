def rev(bi):
    s = str(bi)[::-1]
    return int(s)

def lychrel(n):
    res = None
    cache = {}
    if n in cache:
        return cache[n]

    r = rev(n)
    res = (True, n)
    seen = []

    for i in range(500):
        n = n + r
        r = rev(n)

        if n == r:
            res = (False, 0)
            break

        if n in cache:
            res = cache[n]
            break

        seen.append(n)

    for bi in seen:
        cache[bi] = res

    return res

def main():
    seeds = []
    related = []
    palin = []

    for i in range(1, 10001):
        n = i

        t = lychrel(n)

        if t[0] is False:
            continue

        if n == t[1]:
            seeds.append(t[1])
        else:
            related.append(t[1])

        if n == t[1]:
            palin.append(t[1)

    print(len(seeds), "Lychrel seeds:", seeds)
    print(len(related), "Lychrel related")
    print(len(palin), "Lychrel palindromes:", palin)