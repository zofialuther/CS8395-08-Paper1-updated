def gcd(X, 0, X):
    return X

def gcd(0, X, X):
    return X

def gcd(X, Y, D):
    if X <= Y:
        Z = Y - X
        return gcd(X, Z, D)
    else:
        return gcd(Y, X, D)