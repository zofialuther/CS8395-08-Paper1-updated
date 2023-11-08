```python
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    mersenne_number = 2**p - 1
    if is_prime(mersenne_number):
        return True
    else:
        return False

def main(upper_bound):
    for p in range(2, upper_bound + 1):
        if is_mersenne_prime(p):
            print(2**p - 1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        upper_bound = int(sys.argv[1])
        main(upper_bound)
    else:
        print("Usage: python mersenne.py <upper_bound>")
```