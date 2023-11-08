def p(N, X):
    if N == 0:
        X = 1
    elif N > 0:
        A = 0
        B = 0
        K = 1
        while True:
            M = K * (3 * K - 1) // 2
            if M > N:
                break
            else:
                L = N - M
                Y = p(L, Y)
                Z = (-1) ** K * Y
                A += Z
            K += 1
        
        K = 1
        while True:
            M = K * (3 * K + 1) // 2
            if M > N:
                break
            else:
                L = N - M
                Y = p(L, Y)
                Z = (-1) ** K * Y
                B += Z
            K += 1
        
        X = -A - B