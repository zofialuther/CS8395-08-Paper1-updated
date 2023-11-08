```python
def ft_rows(n):
    row = [1]
    for m in range(1, n+1):
        row.append(0)
        for j in range(m, 0, -1):
            row[j] = j * (row[j] - row[j-1])
    return row

def show(rows):
    for row in rows:
        print(row)

def horner(a, x, n):
    result = a[n]
    for i in range(n-1, -1, -1):
        result = result * x + a[i]
    return result

def drop(a, n):
    return [a[i] for i in range(n, len(a))]

def sum(k):
    row = ft_rows(k+2)
    return horner(drop(row, 1), 1, k+2)
```