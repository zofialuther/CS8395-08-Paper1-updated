from decimal import Decimal, getcontext

def agm(a, g, tolerance=Decimal("1e-65")):
    getcontext().prec = 70
    while True:
        a, g = (a + g) / 2, (a * g).sqrt()
        if abs(a - g) < tolerance:
            return a

result = agm(Decimal(1), 1 / Decimal(2).sqrt())
print(result)