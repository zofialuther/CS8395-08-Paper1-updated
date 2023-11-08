from math import isqrt
import math

def isqrt(x):
    if x < 0:
        raise ValueError("Argument cannot be negative")
    q = 1
    while q * q <= x:
        q *= 2
    z = x
    r = 0
    while q > 1:
        q //= 2
        t = z
        t -= r
        t -= q
        r //= 2
        if t >= 0:
            z = t
            r += q
    return r

print("The integer square root of integers from 0 to 65 are:")
for i in range(66):
    print(isqrt(i), end=' ')
print()

print("The integer square roots of powers of 7 from 7^1 up to 7^73 are:")
print("power                                    7 ^ power                                                 integer square root")
print("----- --------------------------------------------------------------------------------- -----------------------------------------")
pow7 = 7
bi49 = 49
for i in range(1, 74, 2):
    print(f"{i} {pow7 ** i: ,} {isqrt(pow7 ** i): ,}")
    pow7 *= bi49