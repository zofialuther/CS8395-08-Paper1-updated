def sieve(p, xs):
    if not xs:
        return []
    else:
        return [p] + sieve([x for x in xs if x % p > 0])

# Example usage
print(sieve(2, [2, 3, 4, 5, 6, 7, 8, 9, 10]))