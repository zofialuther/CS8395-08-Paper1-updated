def chineseRemainder(n, a):
    prod = 1
    for i in n:
        prod *= i

    p = 0
    sm = 0
    for i in range(len(n)):
        p = prod // n[i]
        sm += a[i] * mulInv(p, n[i]) * p
    
    return sm % prod

def mulInv(a, b):
    b0 = b
    x0 = 0
    x1 = 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        amb = a % b
        a = b
        b = amb
        xqx = x1 - q * x0
        x1 = x0
        x0 = xqx
    
    if x1 < 0:
        x1 += b0
    
    return x1

n = [3, 5, 7]
a = [2, 3, 2]
print(chineseRemainder(n, a))