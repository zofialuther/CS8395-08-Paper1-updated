def lcm(x, y):
    if y == 0:
        return 0
    if x == 0:
        return 0
    return abs(((x // gcd(x, y)) * y))