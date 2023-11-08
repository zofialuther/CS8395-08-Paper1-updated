def modInv(a, m):
    def gcdExt(a, b):
        if b == 0:
            return (1, 0, a)
        else:
            q, r = divmod(a, b)
            s, t, g = gcdExt(b, r)
            return t, s - q * t, g

    i, _, g = gcdExt(a, m)
    
    def mkPos(x):
        if x < 0:
            return x + m
        else:
            return x

    if g == 1:
        return mkPos(i)
    else:
        return None

print(modInv(2, 4))
print(modInv(42, 2017))