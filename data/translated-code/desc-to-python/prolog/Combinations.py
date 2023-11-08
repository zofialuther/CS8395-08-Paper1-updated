def comb_Prolog(L, M, N):
    if len(L) != M:
        return False

    def fill(lst, n):
        if n == 0:
            return lst
        else:
            lst.append(n)
            return fill(lst, n-1)

    for num in L:
        if num < 1 or num > N:
            return False

    return True