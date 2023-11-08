def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    d = 5
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
        if n % d == 0:
            return False
        d += 4
    return True

def count_prime_factors(n):
    if n == 1:
        return 0
    if is_prime(n):
        return 1
    count = 0
    f = 2
    while True:
        if n % f == 0:
            count += 1
            n //= f
            if n == 1:
                return count
            if is_prime(n):
                f = n
        elif f >= 3:
            f += 2
        else:
            f = 3

def main():
    max = 120
    print(f"The attractive numbers up to and including {max} are:")
    count = 0
    for i in range(1, max+1):
        n = count_prime_factors(i)
        if is_prime(n):
            print(f"{i:4d}", end=" ")
            count += 1
            if count % 20 == 0:
                print()
    print()

if __name__ == "__main__":
    main()