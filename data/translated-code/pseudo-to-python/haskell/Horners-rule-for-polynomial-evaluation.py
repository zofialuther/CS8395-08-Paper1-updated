def horner(x, coefficients):
    result = 0
    for coefficient in reversed(coefficients):
        result = coefficient + result * x
    return result

print(horner(3, [-19, 7, -4, 6]))