```python
import math

def isqrt(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main():
    print("Number\tSquare Root")
    for i in range(66):
        print(f"{i}\t{isqrt(i)}")
    for j in range(1, 74):
        num = 7 ** j
        print(f"{num}\t{isqrt(num)}")

if __name__ == "__main__":
    main()
```