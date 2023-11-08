```python
def stirling2(n, k, memo={}):
    if k == 1 or k == n:
        return 1
    if k > n:
        return 0
    if (n, k) in memo:
        return memo[(n, k)]
    memo[(n, k)] = k * stirling2(n-1, k, memo) + stirling2(n-1, k-1, memo)
    return memo[(n, k)]

def main():
    table = []
    for n in range(1, 6):
        row = []
        for k in range(1, n+1):
            row.append(stirling2(n, k))
        table.append(tuple(row))
    for row in table:
        print(' '.join(str(x) for x in row))
    max_val = max(stirling2(100, k) for k in range(1, 101))
    print(max_val)

if __name__ == "__main__":
    main()
```