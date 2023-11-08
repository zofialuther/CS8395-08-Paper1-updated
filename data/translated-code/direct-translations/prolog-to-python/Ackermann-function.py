def ack(M, N, P):
    if M == 0:
        P = N + 1
    elif M > 0 and N == 0:
        P = ack(M - 1, 1)
    elif M > 0 and N > 0:
        S = ack(M, N - 1)
        P = ack(M - 1, S)
    return P

# Example input/output:
result = ack(1, 2)
print(result)  # Output: 4