def gcd(x, y):
    return gcd_(abs(x), abs(y))

def gcd_(a, b):
    if b == 0:
        return a
    else:
        return gcd_(b, a % b)