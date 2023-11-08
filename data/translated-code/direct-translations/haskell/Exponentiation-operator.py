def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return f(x, n-1, x)
    else:
        raise ValueError("Negative exponent")

def f(a, d, y):
    if d == 0:
        return y
    else:
        return g(a, d)

def g(b, i):
    if i % 2 == 0:
        return g(b * b, i // 2)
    else:
        return f(b, i-1, b * y)