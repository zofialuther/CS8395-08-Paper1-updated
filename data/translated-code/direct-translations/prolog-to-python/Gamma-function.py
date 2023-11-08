def gamma_coefficients(coefficients):
    return coefficients


def tolerance(value):
    return value


def gamma(x, _):
    if x <= 0.0:
        return False
    elif x < 1.0:
        return small_gamma(x, y)
    elif x == 1 or x == 1.0:
        return 1
    else:
        x1 = x - 1
        return x1 * gamma(x1, y1)


def small_gamma(x, y):
    Cs = gamma_coefficients()
    return 1 / recip_gamma(x, 1.0, Cs, 1.0, 0.0, y0)


def recip_gamma(_, _, [], _, y, y):
    return y
   

def recip_gamma(_, _, [], x0, x1, y):
    tol = tolerance(1e-17)
    if abs(x1 - x0) < tol:
        return x1
    else:
        return y


def recip_gamma(x, prev_pow, coefficients, _, x1, y):
    power = prev_pow * x
    x2 = x1 + c * power
    return recip_gamma(x, power, coefficients, x1, x2, y)