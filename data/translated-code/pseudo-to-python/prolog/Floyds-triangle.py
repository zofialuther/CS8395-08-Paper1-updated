def floyd(N):
    for I in range(1, N+1):
        for J in range(1, I+1):
            Last = N * (N-1)//2 + J
            V = I * (I-1) //2 + J
            C = get_column(Last)
            AR = f"    {C} {V}| "
            AF = AR
            print(AF)
        print('\n')

def get_column(Last):
    N1 = str(Last)
    return len(N1)