def gcd(u, v):
    if v != 0:
        return gcd(v, u % v)
    else:
        return abs(u)