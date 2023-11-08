def show(Limit):
    for (P1, P2, P3, C) in carmichael(Limit):
        print(f"{P1} * {P2} * {P3}        = {C}")

def carmichael(Upto):
    result = []
    for P1 in range(2, Upto + 1):
        if prime(P1):
            Limit = P1 - 1
            for H3 in range(2, Limit):
                MaxD = H3 + P1 - 1
                for D in range(1, MaxD + 1):
                    if (H3 + P1) * (P1 - 1) % D == 0 and (-P1 * P1) % H3 == D % H3:
                        P2 = 1 + (P1 - 1) * (H3 + P1) // D
                        if prime(P2):
                            P3 = 1 + P1 * P2 // H3
                            if prime(P3):
                                X = P1 * P2 * P3
                                result.append((P1, P2, P3, X))
    return result

def wheel235(L):
    W = [4, 2, 4, 2, 4, 6, 2, 6]
    L = [1, 2, 2] + W

def prime(N):
    if N >= 2:
        wheel235(W)
        return prime(N, 2, W)
    else:
        return False

def prime(N, D, W):
    if D * D > N:
        return True
    else:
        if N % D != 0:
            D2 = D + W[0]
            return prime(N, D2, W[1:])
        else:
            return False
 