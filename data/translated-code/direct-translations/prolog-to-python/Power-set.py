def powerset(X, Y):
    Y = [S for S in subseq(X)]
    
def subseq(X, Y):
    if X == []:
        return []
    elif X == [] or X[1:]:
        return subseq(X[1:], Y)
    elif X[0] == Y[0]:
        return subseq(X[1:], Y[1:])
    else:
        return subseq(X[1:], Y) + subseq(X, Y[1:])