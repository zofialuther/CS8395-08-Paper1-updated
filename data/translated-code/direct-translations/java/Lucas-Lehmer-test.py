from math import sqrt

def isPrime(p):
    if p == 2:
        return True
    elif p <= 1 or p % 2 == 0:
        return False
    else:
        to = int(sqrt(p))
        for i in range(3, to+1, 2):
            if p % i == 0:
                return False
        return True

def isMersennePrime(p):
    if p == 2:
        return True
    else:
        m_p = pow(2, p) - 1
        s = 4
        for i in range(3, p+1):
            s = (s * s - 2) % m_p
        return s == 0

def main():
    upb = 500
    print("Finding Mersenne primes in M[2.." + str(upb) + "]:\nM2 ", end='')
    for p in range(3, upb+1, 2):
        if isPrime(p) and isMersennePrime(p):
            print(" M" + str(p), end='')
    print()

if __name__ == "__main__":
    main()