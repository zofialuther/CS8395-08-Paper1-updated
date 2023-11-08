```python
import math
import random

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def pierpont_primes(n, first):
    primes = []
    if first:
        primes.append(2)
        n -= 1
    two = 2
    two_test = two
    three = 3
    three_test = three
    two_index, three_index = 0, 0
    two_smooth = []
    one = 1
    m_one = -1
    count = 0
    while count < n:
        min_val = min(two_test, three_test)
        two_smooth.append(min_val)
        if min_val == two_test:
            two_test = two * two_smooth[two_index]
            two_index += 1
        if min_val == three_test:
            three_test = three * two_smooth[three_index]
            three_index += 1
        test = min_val + (one if first else m_one)
        if miller_rabin(test, 10):
            primes.append(test)
            count += 1
    return primes

def display(message, primes):
    print(message)
    for i in range(len(primes)):
        print(f"{primes[i]:10}", end=" ")
        if (i + 1) % 10 == 0:
            print()
    print()

def main():
    print("First 50 Pierpont primes of the first kind:")
    display(pierpont_primes(50, True))
    print("First 50 Pierpont primes of the second kind:")
    display(pierpont_primes(50, False))
    print(f"250th Pierpont prime of the first kind:     {pierpont_primes(250, True)[249]:,}")
    print(f"250th Pierpont prime of the second kind: {pierpont_primes(250, False)[249]:,}")

if __name__ == "__main__":
    main()
```