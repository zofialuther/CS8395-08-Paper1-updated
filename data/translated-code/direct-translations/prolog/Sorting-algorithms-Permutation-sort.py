def permutation_sort(L, S):
    if permutation(L, S) and sorted(S):
        return True
    else:
        return False

def sorted(arr):
    if len(arr) <= 1:
        return True
    else:
        return arr[0] <= arr[1] and sorted(arr[1:])

def permutation(L, S):
    if len(L) == 0 and len(S) == 0:
        return True
    elif len(L) > 0:
        X = L[0]
        XS = L[1:]
        ZS = []
        for i in range(len(S)):
            if S[i] != X:
                ZS.append(S[i])
        return permutation(XS, ZS)