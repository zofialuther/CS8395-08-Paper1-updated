def knapsack():
    L = [('item1', 5, 10), ('item2', 8, 12), ('item3', 3, 5)]
    S0 = "initial state"
    N = len(L)
    LN = list(range(1, N+1))
    create_constraint_N(LN, L, S0, S1, [], LW, [], LV)
    S2 = S1.constraint(LW <= 15.0)
    S3 = S2.maximize(LV)
    Len = sum([len(item[0]) for item in L])
    A1 = '~~' + str(Len) + '~~t~~~w|'
    A2 = '~~t~~2f~~~w|'
    A3 = '~~t~~2f~~~w|'
    print_results(S3, A1, A2, A3, L, LN, 0, 0)

def create_constraint_N(HN, TN, L, S1, SF, LW, LWF, LV, LVF):
    if len(HN) == 0 and len(TN) == 0:
        return LW, LV, LWF, LVF
    else:
        S2 = S1.constraint([x(HN)] >= 0)
        S3 = S2.constraint([x(HN)] <= W)
        X = V / W
        return create_constraint_N(HN[1:], TN[1:], L, S1, SF, LW, LWF, LV, LVF)

def compute_lenword(Name, W, V):
    if len(Name) == 0:
        return N
    if len(Name) > N:
        N = len(Name)
    return compute_lenword(Name[1:], W, V)

def print_results(S, A1, A2, A3, Name, W, V):
    if S == "":
        print(A1.format('', 0))
        print(A2.format('', 0))
        print(A3.format('', 0))
    else:
        X = S.value(x(N))
        if X == 0:
            W1 = 0
            V1 = 0
        else:
            Vtemp = X * V / W
            W2 = 0
            V2 = 0
        print_results(S, A1, A2, A3, Name, W, V)