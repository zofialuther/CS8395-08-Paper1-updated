def comb_Prolog(L, M, N):
    if len(L) == M:
        fill(L, 1, N)

def fill([], _, _):
    pass

def fill(L, Min, Max):
    if not L:
        return
    else:
        for i in range(Min, Max+1):
            L[0] = i
            fill(L[1:], i+1, Max)