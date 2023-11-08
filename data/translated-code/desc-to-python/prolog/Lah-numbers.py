```python
cache = {}

def lah(n, k):
    if k == 0:
        return 1 if n == 0 else 0
    if n < k:
        return 0
    if (n, k) in cache:
        return cache[(n, k)]
    result = (n - k + 1) * lah(n - 1, k - 1) + (k + 1) * lah(n - 1, k)
    cache[(n, k)] = result
    return result

def print_lah(limit):
    for n in range(limit + 1):
        for k in range(n + 1):
            print(lah(n, k), end=" ")
        print()

def max_lah(n):
    max_val = 0
    for k in range(n + 1):
        val = lah(n, k)
        if val > max_val:
            max_val = val
    return max_val

def main():
    print("Printing Lah numbers up to L(12, 12):")
    print_lah(12)
    print("Maximum value of L(n,k) where n = 100:", max_lah(100))

if __name__ == "__main__":
    main()
```