def modInv(a, m):
    if 1 == gcdExt(a, m)[2]:
        x = mkPos(gcdExt(a, m)[0])
        return x
    else:
        return None

def gcdExt(a, b):
    if b == 0:
        x = 1
        y = 0
        g = a
    else:
        q, r = divmod(a, b)
        s, t, g = gcdExt(b, r)
        x = t
        y = s - q * t
    return x, y, g

def mkPos(x):
    if x < 0:
        x = x + m
    return x

def main():
    print(modInv(2, 4))
    print(modInv(42, 2017))