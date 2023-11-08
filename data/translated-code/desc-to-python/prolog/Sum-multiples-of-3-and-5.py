def sum_of_multiples_of_3_and_5_slow(N, TT):
    return sum_of_multiples_of_3_and_5(1, 0, N, TT)

def sum_of_multiples_of_3_and_5(K, S, N, TT):
    if K >= N:
        return TT
    elif K % 3 == 0 or K % 5 == 0:
        TT += K
    return sum_of_multiples_of_3_and_5(K+1, S, N, TT)