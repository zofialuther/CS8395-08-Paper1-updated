def factors(N, FList):
    factors(N, 2, 0, FList)

def factors(1, _, _Count, []):
    pass
def factors(_, _, Count, []):
    if Count > 1:
        pass
def factors(N, Start, Count, [Fac, *FList]):
    N1 = int(N ** 0.5)
    for Fac in range(Start, N1 + 1):
        if N % Fac == 0:
            N2 = N // Fac
            Count1 = Count + 1
            factors(N2, Fac, Count1, FList)
def factors(N, _, _, [N]):
    if N >= 2:
        pass

def semiPrimeList(Limit, List):
    List = [N for N in semiPrimes(2, Limit)]
    return List

def semiPrimes(Start, Limit, N):
    for N in range(Start, Limit + 1):
        if factors(N, [F1, F2]) and N == F1 * F2:
            yield N

def do():
    SemiPrimes = semiPrimeList(100)
    print(SemiPrimes)
    SemiPrimes2 = [N for N in semiPrimes(1675, 1685)]
    print(SemiPrimes2)