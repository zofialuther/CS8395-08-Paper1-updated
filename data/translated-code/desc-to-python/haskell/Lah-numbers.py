```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def lah_number(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def print_lah_numbers(rows):
    for n in range(1, rows+1):
        for k in range(1, n+1):
            print(lah_number(n, k), end="\t")
        print()

def main():
    print_lah_numbers(10)
    max_lah = max([lah_number(100, k) for k in range(1, 101)])
    print("Maximum value from L(100, *) row of Lah numbers:", max_lah)

if __name__ == "__main__":
    main()
```