def primes(n):
    multiples = set()
    prime = []
    for i in range(2, n+1):
        if i not in multiples:
            prime.append(i)
            multiples.update(set(range(i*i, n+1, i)))
    return prime

def truncatableprime(n):
    primelist = [str(x) for x in reversed(primes(n))]
    primeset = set(primelist)
    for num in primelist:
        alltruncs = set([num[i:] for i in range(len(num))])
        if alltruncs.issubset(primeset):
            truncateleft = int(num)
            break
    for num in primelist:
        alltruncs = set([num[:i+1] for i in range(len(num))])
        if alltruncs.issubset(primeset):
            truncateright = int(num)
            break
    return truncateleft, truncateright

maxprime = 1000000
print(truncatableprime(maxprime))