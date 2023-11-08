def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(p, q, n):
    if p <= n:
        return True
    q1 = p % n
    if is_prime(q1) and q != q1:
        n1 = n * 10
        return is_left_truncatable_prime(p, q1, n1)
    return False

def largest_left_truncatable_prime(n, p):
    if is_left_truncatable_prime(n, n, 10):
        return n
    elif n > 1:
        n1 = n - 1
        return largest_left_truncatable_prime(n1, p)

def is_right_truncatable_prime(p):
    if is_prime(p):
        q = p // 10
        if q == 0:
            return True
        else:
            return is_right_truncatable_prime(q)
    return False

def largest_right_truncatable_prime(n, p):
    if is_right_truncatable_prime(n):
        return n
    elif n > 1:
        n1 = n - 1
        return largest_right_truncatable_prime(n1, p)

def main(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    l = largest_left_truncatable_prime(n, n)
    r = largest_right_truncatable_prime(n, n)
    print(f'Largest left-truncatable prime less than {n}: {l}')
    print(f'Largest right-truncatable prime less than {n}: {r}')

main(1000000)