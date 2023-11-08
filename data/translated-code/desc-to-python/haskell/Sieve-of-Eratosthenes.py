def primes(n):
    def sieve(m):
        sieve = [True] * (m // 2)
        for i in range(3, int(m ** 0.5) + 1, 2):
            if sieve[i // 2]:
                sieve[i * i // 2::i] = [False] * ((m - i * i - 1) // (2 * i) + 1)
        return [2] + [2 * i + 1 for i in range(1, m // 2) if sieve[i]]

    def gaps(pl):
        for p in pl:
            if p - pl[-1] > 2:
                yield from range(pl[-1] + 2, p, 2)

    def primes():
        yield 2
        pl = [2]
        yield from pl
        while True:
            pl = sieve(2 * pl[-1])
            yield from gaps(pl)
            yield from pl

    return list(itertools.takewhile(lambda x: x <= n, primes()))