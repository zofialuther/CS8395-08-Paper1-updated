```python
def main():
    # usage
    pas(20)

def pas(rows):
    for i in range(rows):
        for j in range(i+1):
            print(ncr(i, j), end=" ")
        print()

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

if __name__ == "__main__":
    main()
```