def isqrt(x):
    if x < 0:
        raise ValueError("Argument cannot be negative")
    q = 1
    while q <= x:
        q = q * 4
    z = x
    r = 0
    while q > 1:
        q = q // 4
        t = z
        t = t - r
        t = t - q
        r = r // 2
        if t >= 0:
            z = t
            r = r + q
    return r

def main(args):
    print("The integer square root of integers from 0 to 65 are:")
    for i in range(66):
        print(isqrt(i))

    print("The integer square roots of powers of 7 from 7^1 up to 7^73 are:")
    print("power                                    7 ^ power                                                 integer square root")
    print("----- --------------------------------------------------------------------------------- -----------------------------------------")
    pow7 = 7
    bi49 = 49
    for i in range(1, 74, 2):
        print(i, pow7, isqrt(pow7))
        pow7 = pow7 * bi49