def gcd(u, v):
    if v:
        return gcd(v, u % v)
    else:
        return abs(u)