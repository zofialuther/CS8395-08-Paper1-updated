def sum_of_multiples_of_3_and_5_slow(N, TT):
    sum_of_multiples_of_3_and_5(N, 1, 0, TT)

def sum_of_multiples_of_3_and_5(N, K, S, S):
    return 3 * K >= N

def sum_of_multiples_of_3_and_5(N, K, C, S):
    T3 = 3 * K
    if T3 >= N:
        return S
    else:
        C3 = C + T3
        T5 = 5 * K
        if T5 < N and K % 3 != 0:
            C5 = C3 + T5
        else:
            C5 = C3
        K1 = K + 1
        return sum_of_multiples_of_3_and_5(N, K1, C5, S)