def sum_of_multiples_of_3_and_5_slow(N, TT):
    sum_of_multiples_of_3_and_5(N, 1, 0, TT)

def sum_of_multiples_of_3_and_5(N, K, S, TT):
    if 3 * K >= N:
        TT = S
    else:
        T3 = 3 * K
        if T3 < N:
            C3 = S + T3
            T5 = 5 * K
            if T5 < N and K % 3 != 0:
                C5 = C3 + T5
            else:
                C5 = C3
            K1 = K + 1
            sum_of_multiples_of_3_and_5(N, K1, C5, TT)