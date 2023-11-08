def gcd(X, Y):
    if Y == 0:
        return X
    else:
        return gcd(Y, X % Y)