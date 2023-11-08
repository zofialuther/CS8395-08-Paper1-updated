def isPrime(A):
    A1 = math.ceil(math.sqrt(A))
    for N in range(2, A1):
        if A % N == 0:
            return False
    return True

def divisors(N, Dlist):
    N1 = math.floor(math.sqrt(N))
    Ds0 = list(range(1, N1+1))
    Ds1 = []
    for D in Ds0:
        if N % D == 0:
            Ds1.append(D)
    Ds1.reverse()
    if Ds1[0] * Ds1[0] < N:
        Ds1a = Ds1
    else:
        Ds1a = Ds1[1:]
    Ds2 = [N // D for D in Ds1a]
    Dlist = Ds1 + Ds2

def longPrime(P):
    Dlist = divisors(P - 1)
    for D in Dlist:
        if pow(10, D, P) != 1:
            return False
    return Dlist[-1] == P - 1

def isLongPrime(N):
    if isPrime(N) and longPrime(N):
        return True
    else:
        return False

def longPrimes(N, LongPrimes):
    List = list(range(7, N+1))
    LongPrimes = [x for x in List if isLongPrime(x)]

def run(LimitList):
    return

def run(LimitList):
    Start = current_time()
    LongPrimes = longPrimes(Limit)
    Num = len(LongPrimes)
    Stop = current_time()
    Runtime = Stop - Start
    print("There are {} long primes up to {} [time (ms) {}]".format(Num, Limit, Runtime))
    run(Tail)

def do():
    LongPrimes = longPrimes(500)
    print('long primes up to 500:')
    print(LongPrimes)
    LimitList = [500 * 2**x for x in range(8)]
    run(LimitList)