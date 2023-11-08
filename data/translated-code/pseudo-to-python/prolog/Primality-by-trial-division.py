def prime(N):
    if N == 2:
        return True
    elif N > 2:
        for i in range(3, N+1):
            if N % 2 == 1:
                M = int((N+1)**0.5)
                Max = (M-1) // 2
                for j in range(1, Max+1):
                    if N % (2*j+1) <= 0:
                        return False
        return True