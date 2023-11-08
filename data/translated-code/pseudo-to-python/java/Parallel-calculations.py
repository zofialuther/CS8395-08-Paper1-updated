```python
from multiprocessing import Pool
import math

NUMBERS = [
    12757923,
    12878611,
    12878893,
    12757923,
    15808973,
    15780709,
    197622519
]

def minimalPrimeFactor(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return (i, n)
    return (n, n)

def main():
    with Pool(processes=4) as pool:
        results = pool.map(minimalPrimeFactor, NUMBERS)
        max_result = max(results, key=lambda x: x[0])
        print(f"{max_result[1]} has the largest minimum prime factor: {max_result[0]}")

if __name__ == "__main__":
    main()
```