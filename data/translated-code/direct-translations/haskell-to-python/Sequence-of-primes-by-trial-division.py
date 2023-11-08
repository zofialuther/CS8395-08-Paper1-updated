from itertools import islice

def sieve():
    yield 2
    yield 3
    ps = sieve()
    p = next(ps)
    psq = p * p
    init = islice(ps, 0, p - 2)
    for i in count(p + 2, 2):
        if i >= psq:
            p = next(ps)
            psq = p * p
            init = islice(ps, 0, p - 2)
        if all(i % p for p in init):
            yield i