def nPrimes(M, Primes):
    nPrimes([2], M, Primes)

def nPrimes(Accumulator, I, Primes):
    prime = next_prime(Accumulator)
    next = Accumulator + [prime]
    N = len(next)
    if N == I:
        Primes = next
    else:
        nPrimes(next, I, Primes)

def next_prime(primes):
    if primes == [2]:
        return 3
    else:
        PP = primes[-1]
        P2 = PP + 2
        N = generate(P2)
        if N % 2 == 1:
            Max = int((N+1)**0.5)
            for prime in [2] + primes:
                if prime <= Max:
                    if N % prime == 0:
                        break
            else:
                return N

def multiply(A, lst):
    return [A * x for x in lst]

def multiplylist(lst1, lst2):
    if not lst1:
        return []
    else:
        L1 = multiply(lst1[0], lst2)
        L2 = multiplylist(lst1[1:], lst2)
        return L1 + L2

def take(N, lst):
    return lst[:N]