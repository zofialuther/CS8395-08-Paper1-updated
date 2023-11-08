def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_partition(N, K, primes, Min):
    if K == 1:
        if is_prime(N) and N > Min:
            return True
    else:
        for i in range(len(primes)):
            if is_prime(primes[i]) and primes[i] > Min and primes[i] < N:
                if prime_partition(N - primes[i], K - 1, primes[i+1:], primes[i]):
                    return True
    return False

def print_primes(primes):
    if len(primes) == 1:
        print(primes[0])
    else:
        for i in range(len(primes) - 1):
            print(primes[i], end=" + ")
        print(primes[-1])

def print_prime_partition(N, K):
    primes = [2]
    for num in range(3, N + 1):
        if is_prime(num):
            primes.append(num)
    if prime_partition(N, K, primes, 1):
        print(f"{N} = ", end="")
        print_primes(primes)
    else:
        print(f"{N} cannot be partitioned into {K} primes.")

def main():
    print_prime_partition(99809, 1)
    print_prime_partition(18, 2)
    print_prime_partition(19, 3)
    print_prime_partition(20, 4)
    print_prime_partition(2017, 24)
    print_prime_partition(22699, 1)
    print_prime_partition(22699, 2)
    print_prime_partition(22699, 3)
    print_prime_partition(22699, 4)
    print_prime_partition(40355, 3)

main()