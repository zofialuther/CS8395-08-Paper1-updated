import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_up_to(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_prime_combinations(primes, target_sum):
    for r in range(1, len(primes) + 1):
        for combination in itertools.combinations(primes, r):
            if sum(combination) == target_sum:
                print(combination)
                return
    print("No combination is possible")

# Example usage
primes_list = generate_primes_up_to(20)
find_prime_combinations(primes_list, 10)