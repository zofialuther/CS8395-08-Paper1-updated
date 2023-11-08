```python
from functools import lru_cache

@lru_cache(maxsize=None)
def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return k * stirling2(n-1, k) + stirling2(n-1, k-1)

def stirling2_3(n, k):
    return stirling2(n, k)

def print_stirling_numbers(n):
    for i in range(n+1):
        for j in range(i+1):
            print(stirling2(i, j), end=' ')
        print()

def max_stirling2(n):
    max_val = 0
    for i in range(n+1):
        for j in range(i+1):
            max_val = max(max_val, stirling2(i, j))
    return max_val

def main():
    print_stirling_numbers(12)
    print(max_stirling2(100))

if __name__ == "__main__":
    main()
```