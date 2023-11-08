def prime_factors(m=2):
    factors = []
    for i in range(2, m):
        r, q = divmod(m, i)
        if q != 0:
            return [i] + prime_factors(r)
    return [m]

def k_almost_primes(n, k=2):
    multiples = set()
    lists = []
    for x in range(k):
        lists.append([])

    for i in range(2, n):
        if i not in multiples:
            if len(lists[0]) < 10:
                lists[0].append(i)
            multiples.update(range(i*i, n+1, i))
    print("k=1: {}".format(lists[0]))

    for j in range(1, k):
        for m in multiples:
            l = prime_factors(m)
            ll = len(l)
            if ll == j and len(lists[j]) < 10:
                lists[j].append(m)
        print("k={}: {}".format(j+1, lists[j]))

k_almost_primes(200, 5)