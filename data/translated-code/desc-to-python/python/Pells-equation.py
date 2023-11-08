import math

def solvePell(n):
    m = 1
    a = int(math.sqrt(n))
    if a * a == n:
        return None
    den = 1
    num = a
    x1 = 1
    x = num
    y1 = 0
    y = 1
    while x * x - n * y * y != 1:
        m = den * a - m
        den = (n - m * m) / den
        a = int((a + m) / den)
        num, x1 = x1, x
        x = num * x1 + a * x
        y1, y = y, num * y1 + a * y
    return x, y

print(solvePell(61))
print(solvePell(109))
print(solvePell(181))
print(solvePell(277))