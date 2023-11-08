def comb_Prolog(L, M, N):
    length(L, M)
    fill(L, 1, N)

def fill(L, _, _):
    pass

def fill(L, Min, Max):
    if L[0] >= Min and L[0] <= Max:
        H1 = L[0] + 1
        fill(L[1:], H1, Max)