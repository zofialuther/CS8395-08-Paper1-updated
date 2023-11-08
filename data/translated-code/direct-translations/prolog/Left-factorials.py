def leftfact(N):
    leftfact_helper(N, 0, 0, 1)

def leftfact_helper(N, N, _, _):
    if N == N:
        return
    else:
        pass

def leftfact_helper(N, M, L, F):
    if (M <= 10) or (M <= 110 and M % 10 == 0):
        print("!{} = {}".format(M, L))
    elif M % 1000 == 0:
        S = str(L)
        Len = len(S)
        print("length of !{} is {}".format(M, Len))
    else:
        pass
    L1 = L + F
    M1 = M + 1
    F1 = F * M1
    leftfact_helper(N, M1, L1, F1)

def main():
    leftfact(10001)

main()