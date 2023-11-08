```python
import fractran

def is_prime(num):
    binary = bin(num)[2:]
    return binary.count('1') == 1 and binary.count('0') > 1

def generate_primes():
    prog = fractran.Program([17 / 91, 78 / 85, 19 / 51, 23 / 38, 29 / 33, 77 / 29, 95 / 23, 77 / 19, 1 / 17, 11 / 13, 13 / 11, 15 / 2, 1 / 7, 55 / 1])
    series = prog.iterate(2)
    for i, num in enumerate(series):
        if is_prime(num):
            yield num, i

if __name__ == "__main__":
    for prime, position in generate_primes():
        print(f"Prime number {prime} found at position {position} in the series.")
```