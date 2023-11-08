def nthRoot(n, x):
    result = x
    x0 = x / n
    while abs(result - x0) >= 0.0001:
        result = x0
        x0 = ((n - 1) * x0 + x / (x0 ** (n - 1))) / n
    return result