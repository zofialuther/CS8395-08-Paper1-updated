def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return helperFunction(base, exponent-1, base)
    else:
        raise ValueError("Prelude.^: negative exponent")

def helperFunction(a, d, y):
    if d == 0:
        return y
    else:
        return innerFunction(a, d, y)

def innerFunction(b, i, y):
    if i % 2 == 0:
        return innerFunction(b*b, i//2, y)
    else:
        return helperFunction(b, i-1, b*y)