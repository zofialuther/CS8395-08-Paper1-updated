```python
import itertools
import operator

def binary_to_gray(n):
    return n ^ (n >> 1)

def gray_to_binary(n):
    n = n ^ (n >> 16)
    n = n ^ (n >> 8)
    n = n ^ (n >> 4)
    n = n ^ (n >> 2)
    n = n ^ (n >> 1)
    return n

def display_results(num, binary, gray):
    print(f"Decimal: {num}, Binary: {binary}, Gray Code: {gray}")

def main():
    for num in range(10):
        binary = bin(num)[2:].zfill(4)
        gray = bin(binary_to_gray(num))[2:].zfill(4)
        display_results(num, binary, gray)

if __name__ == "__main__":
    main()
```