def horner(x, coefficients):
    return reduce(lambda b, a: a + b*x, coefficients, 0)

print(horner(3, [-19, 7, -4, 6]))