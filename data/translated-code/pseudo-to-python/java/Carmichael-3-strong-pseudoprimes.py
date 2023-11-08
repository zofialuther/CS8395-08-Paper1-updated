def mod(n, m):
    return ((n % m) + m) % m

def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    elif (n < 2) or (n % 2 == 0) or (n % 3 == 0):
        return False
    div = 5
    inc = 2
    while (div ** 2 <= n):
        if (n % div == 0):
            return False
        div = div + inc
        inc = 6 - inc
    return True

def main(args):
    for p in range(2, 62):
        if not isPrime(p):
            continue
        for h3 in range(2, p - 1):
            g = h3 + p
            for d in range(1, g - 1):
                if ((g * (p - 1)) % d != 0) or (mod(-p * p, h3) != d % h3):
                    continue
                q = 1 + (p - 1) * g / d
                if not isPrime(q):
                    continue
                r = 1 + (p * q / h3)
                if (not isPrime(r)) or ((q * r) % (p - 1) != 1):
                    continue
                print(p, q, r)