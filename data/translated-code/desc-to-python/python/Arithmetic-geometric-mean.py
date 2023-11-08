from decimal import Decimal, getcontext

def agm(a, g, tol=1e-70):
    getcontext().prec = 70
    while abs(a - g) > tol:
        a, g = (a + g) / 2, (a * g).sqrt()
    return a

initial_a = Decimal(3)
initial_g = Decimal(4)
result = agm(initial_a, initial_g)
print(result)