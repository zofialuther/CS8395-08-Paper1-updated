def gcd(u, v):
    if v == 0:
        return abs(u)
    else:
        return gcd(v, u % v)