def is_prime(p):
    if p == 2:
        return True
    elif p <= 1 or p % 2 == 0:
        return False
    else:
        for i in range(3, int(p ** 0.5) + 1, 2):
            if p % i == 0:
                return False
        return True

def is_mersenne_prime(p):
    if p == 2:
        return True
    else:
        m_p = (1 << p) - 1
        s = 4
        for i in range(3, p + 1):
            s = (s ** 2 - 2) % m_p
        return s == 0

precision = 20000
upb_prime = int(precision * math.log(10, 2)) / 2
upb_count = 45

print("Finding Mersenne primes in M[2..", upb_prime, "]:")
count = 0
for p in range(2, int(upb_prime) + 1):
    if is_prime(p) and is_mersenne_prime(p):
        print("M", p)
        count += 1
    if count >= upb_count:
        break