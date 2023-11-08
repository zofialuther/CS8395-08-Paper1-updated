def smart_factors(N):
    if not isinstance(N, int):
        return "N must be an integer"
    if N <= 0:
        return "N must be greater than 0"
    
    Fs = set()
    for X in range(1, int(N**0.5)+1):
        if N % X == 0:
            Fs.add(X)
            Fs.add(N // X)
    return sorted(Fs)