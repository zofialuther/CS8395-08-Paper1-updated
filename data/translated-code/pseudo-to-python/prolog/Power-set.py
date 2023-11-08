def powerset(X):
    return [subseq(S, X) for S in range(len(X)+1)]

def subseq(X, Y):
    if len(X) == 0:
        return []
    elif len(Y) == 0:
        return []
    elif X[0] == Y[0]:
        return subseq(X[1:], Y[1:])
    else:
        return subseq(X, Y[1:]) + subseq(X, Y[1:])