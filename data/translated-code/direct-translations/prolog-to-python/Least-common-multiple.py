def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y, z):
    return abs(x * y) // gcd(x, y)