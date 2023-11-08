from itertools import accumulate

def expand(p):
    return list(accumulate(range(1, p+1), lambda z, i: z * (p-i+1) // i, initial=1))

def test(p):
    if p < 2:
        return False
    else:
        return all(n % p == 0 for n in expand(p)[:-1])

def printPoly(p):
    if p == [1]:
        return "1"
    else:
        l = len(p)
        return ''.join([pow(i) + sgn(l-i) + str(p[i-1]) for i in range(l-1, 0, -1)])

def main():
    print("-- p: (x-1)^p for small p")
    print('\n'.join([f"{i}: {printPoly(expand(i))}" for i in range(11)]))
    print("-- Primes up to 100:")
    print([i for i in range(1, 101) if test(i)])

main()