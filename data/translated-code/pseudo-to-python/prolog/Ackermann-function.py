def ack(M, N, P):
    if M == 0:
        return s(N)
    elif N == 0:
        return ack(M-1, s(0), P)
    else:
        S = ack(M, N-1, s(0))
        return ack(M-1, S, P)