def lcm(X, Y, Z):
    from math import gcd
    Z = abs(X*Y) // gcd(X, Y)