def chowla(n):
    if n < 2:
        return 0
    else:
        divisorsList = [x for x in range(1, n+1) if n % x == 0]
        sumOfDivisors = 0
        for divisor in divisorsList:
            sumOfDivisors = sumOfDivisors + divisor
        return sumOfDivisors - 1 - n

def is_prime(n):
    return chowla(n) == 0

def primes_to(n):
    count = 0
    for i in range(2, n):
        if chowla(i) == 0:
            count = count + 1
    return count

def perfect_between(n, m):
    c = 0
    print("Perfect numbers between [" + str(n) + ", " + str(m) + ")")
    for i in range(n, m):
        if i > 1 and chowla(i) == i - 1:
            print("  " + str(i))
            c = c + 1
    print("Found " + str(c) + " Perfect numbers between [" + str(n) + ", " + str(m) + ")")

if __name__ == '__main__':
    for i in range(1, 38):
        print("chowla(" + str(i) + ") == " + str(chowla(i)))
    for i in range(2, 6):
        print("primes_to(" + str(10**i) + ") == " + str(primes_to(10**i)))
    perfect_between(1, 1000000)
    print()
    for i in range(6, 8):
        print("primes_to(" + str(10**i) + ") == " + str(primes_to(10**i)))
    perfect_between(1000000, 35000000)