```python
# Prolog program to find prime partitions of a given number

# Predicate to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Predicate to generate prime partitions
def prime_partitions(n, plist):
    if n == 0:
        return [[]]
    result = []
    for p in plist:
        if p > n:
            break
        if p <= n:
            for pp in prime_partitions(n - p, [x for x in plist if x >= p]):
                result.append([p] + pp)
    return result

# Predicate to print the results
def print_results(num, partitions):
    print(f"Prime partitions of {num}:")
    for partition in partitions:
        print(partition)

# Main function to demonstrate the use of the program
def main():
    numbers = [10, 20, 30]  # Example numbers
    for num in numbers:
        plist = [x for x in range(2, num) if is_prime(x)]
        partitions = prime_partitions(num, plist)
        print_results(num, partitions)

if __name__ == "__main__":
    main()
```