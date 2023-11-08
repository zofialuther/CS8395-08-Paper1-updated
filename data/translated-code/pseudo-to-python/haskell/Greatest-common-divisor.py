def gcd(x, y):
    abs_x = abs(x)
    abs_y = abs(y)
    return gcd_(abs_x, abs_y)

def gcd_(a, 0):
    return a

def gcd_(a, b):
    next_b = a % b
    return gcd_(b, next_b)