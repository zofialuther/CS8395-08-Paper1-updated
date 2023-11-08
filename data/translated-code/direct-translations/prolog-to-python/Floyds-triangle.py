def floyd(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            Last = N * (N-1)/2 + j
            V = i * (i-1) / 2 + j
            C = get_column(Last)
            AR = ' ' * C + str(V) + '| '
            AF = AR
            print(AF, end='')
        print()

def get_column(Last):
    return len(str(Last))