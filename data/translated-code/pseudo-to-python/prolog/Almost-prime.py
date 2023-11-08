def nPrimes(M, Primes):
    nPrimes([2], M, Primes)

def nPrimes(Accumulator, I, Primes):
    Prime = next_prime(Accumulator)
    Next = Accumulator.append(Prime)
    N = len(Next)
    if N == I:
        Primes = Next
    else:
        nPrimes(Next, I, Primes)

def next_prime(Primes):
    if Primes == [2]:
        return 3
    else:
        PP = Primes[-1]
        P2 = PP + 2
        N = generate(P2)
        if N % 2 == 1:
            Max = floor(sqrt(N + 1))
            isPrime = True
            for i in range(2, Max+1):
                if N % i == 0:
                    isPrime = False
                    break
            if isPrime:
                return N

def multiply(A, List, Answer):
    if List == []:
        return []
    else:
        AX = A * List[0]
        As = multiply(A, List[1:])
        return [AX].concat(As)

def multiplylist(L1, L2, List):
    if L1 == []:
        return []
    else:
        L1Result = multiply(L1[0], L2)
        L2Result = multiplylist(L1[1:], L2)
        return L1Result.concat(L2Result)

def take(N, List, Head):
    Head = List[:N]