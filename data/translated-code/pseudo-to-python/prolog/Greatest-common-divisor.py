def gcd(X, Y):
    if Y == 0:
        return X
    elif X == 0:
        return Y
    elif X <= Y:
        Z = Y - X
        return gcd(X, Z)
    else:
        return gcd(Y, X)