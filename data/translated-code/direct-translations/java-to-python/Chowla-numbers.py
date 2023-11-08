```python
import locale

def chowla(n):
    if n < 0:
        raise ValueError("n is not positive")
    sum = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            j = n // i
            sum += i + (0 if i == j else j)
        i += 1
    return sum

def countPrimes(power, limit):
    count = 0
    num = [[0, 0] for _ in range(countMultiplicity(limit, power))]
    i = 0
    for n in range(2, limit+1):
        if chowla(n) == 0:
            count += 1
        if n % power == 0:
            num[i][0] = power
            num[i][1] = count
            i += 1
            power *= 10
    return num

def countMultiplicity(limit, start):
    count = 0
    cur = limit
    while cur >= start:
        count += 1
        cur //= 10
    return count

def findChowlaNumbers(limit):
    num = [0] * limit
    for i in range(limit):
        num[i] = chowla(i+1)
    return num

def findPerfectNumbers(limit):
    count = 0
    num = []

    k = 2
    kk = 3
    p = 0
    while (p := k * kk) < limit:
        if chowla(p) == p - 1:
            num.append(p)
            count += 1
        k = kk + 1
        kk += k
    return num

def increaseArr(arr):
    return arr + [0]

def main():
    chowlaNumbers = findChowlaNumbers(37)
    for i in range(len(chowlaNumbers)):
        print(f"chowla({i+1}) = {chowlaNumbers[i]}")
    print()

    primes = countPrimes(100, 10_000_000)
    for i in range(len(primes)):
        print(locale.format_string("There is %d primes up to %d", (primes[i][1], primes[i][0])))
    print()

    perfectNumbers = findPerfectNumbers(35_000_000)
    for num in perfectNumbers:
        print(f"{num} is a perfect number")
    print(locale.format_string("There are %d perfect numbers < %d", (len(perfectNumbers), 35_000_000)))

if __name__ == "__main__":
    main()
```