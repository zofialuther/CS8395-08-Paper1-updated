def countDivisors(n):
    if n < 2:
        return 1
    count = 2  # 1 and n
    for i in range(2, n//2 + 1):
        if n % i == 0:
            count = count + 1
    return count

def main():
    maxDiv = 0
    count = 0
    print("The first 20 anti-primes are:")
    n = 1
    while count < 20:
        d = countDivisors(n)
        if d > maxDiv:
            print(n)
            maxDiv = d
            count = count + 1
        n = n + 1
    print