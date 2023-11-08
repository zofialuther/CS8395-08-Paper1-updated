from math import sqrt

def is_prime(x):
    if x < 3 or x % 2 == 0:
        return x == 2

    max = int(sqrt(x))
    for n in range(3, max + 1, 2):
        if x % n == 0:
            return False
    return True

def get_primes(start, end):
    return filter(is_prime, range(start, end + 1))

def main():
    primes = list(get_primes(0, 100))
    print(', '.join(map(str, primes)))

if __name__ == "__main__":
    main()