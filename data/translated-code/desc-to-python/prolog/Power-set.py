def powerset(X, Y):
    if X == []:
        Y.append([])
    else:
        powerset(X[1:], Y)
        for subset in Y[:]:
            Y.append([X[0]] + subset)