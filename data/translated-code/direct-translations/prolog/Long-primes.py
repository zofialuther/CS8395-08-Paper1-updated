def isPrime(A):
    A1 = ceil(sqrt(A))
    for N in range(2, A1):
        if A % N == 0:
            return False
    return True

def divisors(N):
    N1 = floor(sqrt(N))
    Ds0 = list(range(1, N1+1))
    Ds1 = [d for d in Ds0 if N % d == 0]
    Ds1.reverse()
    Dh = Ds1[0]
    if Dh * Dh < N:
        Ds1a = Ds1
    else:
        Ds1a = Ds1[1:]
    Ds2 = [N // d for d in Ds1a]
    return Ds1 + Ds2

def longPrime(P):
    Dlist = divisors(P - 1)
    for D in Dlist:
        if pow(10, D, P) != 1:
            return False
    return True

def isLongPrime(N):
    return isPrime(N) and longPrime(N)

def longPrimes(N):
    List = list(range(7, N+1))
    LongPrimes = [num for num in List if isLongPrime(num)]
    return LongPrimes

def run(Tail):
    for limit in Tail:
        start = time.time()
        LongPrimes = longPrimes(limit)
        num = len(LongPrimes)
        stop = time.time()
        runtime = stop - start
        print(f'there are {num} long primes up to {limit} [time (ms) {runtime}]')

def do():
    LongPrimes = longPrimes(500)
    print('long primes up to 500:')
    print(LongPrimes)
    LimitList = [500 * 2**x for x in range(8)]
    run(LimitList)