from math import sqrt, floor
from decimal import Decimal

def pells_equation(n):
    a0 = int(sqrt(n))
    if a0*a0 == n:
        raise ValueError("ERROR 102:  Invalid n = " + str(n))
    continued_frac = continued_fraction(n)
    count = 0
    ajm2 = Decimal(1)
    ajm1 = Decimal(a0)
    bjm2 = Decimal(0)
    bjm1 = Decimal(1)
    stop = (len(continued_frac) % 2 == 1)
    if len(continued_frac) == 2:
        stop = True
    while True:
        count += 1
        bn = Decimal(continued_frac[count])
        aj = bn * ajm1 + ajm2
        bj = bn * bjm1 + bjm2
        if stop and (count == len(continued_frac)-2 or len(continued_frac) == 2):
            return [aj, bj]
        elif len(continued_frac) % 2 == 0 and count == len(continued_frac)-2:
            stop = True
        if count == len(continued_frac)-1:
            count = 0
        ajm2 = ajm1
        ajm1 = aj
        bjm2 = bjm1
        bjm1 = bj

def continued_fraction(n):
    answer = [int(sqrt(n))]
    a0 = int(sqrt(n))
    a = -a0
    a_start = a
    b = 1
    b_start = b
    while True:
        values = iterate_frac(n, a, b)
        answer.append(values[0])
        a = values[1]
        b = values[2]
        if a == a_start and b == b_start:
            break
    return answer

def iterate_frac(n, a, b):
    x = int(floor((b * sqrt(n) - b * a)/(n - a * a)))
    answer = [x, -(b * a + x *(n - a * a)) / b, (n - a * a) / b]
    return answer

format = NumberFormat.getInstance()
for n in [61, 109, 181, 277, 8941]:
    pell = pells_equation(n)
    print("x^2 - %3d * y^2 = 1 for:\n    x = %s\n    y = %s\n" % (n,  format.format(pell[0]),  format.format(pell[1])))