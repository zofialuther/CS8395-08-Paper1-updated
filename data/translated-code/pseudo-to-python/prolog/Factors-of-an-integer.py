def smart_factors(N):
    if isinstance(N, int) and N > 0:
        Fs = set()
        for i in range(1, N+1):
            if N % i == 0:
                Fs.add(i)
        return Fs
    else:
        return "N must be a positive integer"
        
def factor(N):
    L = int(N ** 0.5)
    Fs = set()
    for X in range(1, L+1):
        if N % X == 0:
            Fs.add(X)
            if X != N // X:
                Fs.add(N // X)
    return Fs