```python
def properDivsSum(n):
    return sum(i for i in range(1, (n + 1) // 2 + 1) if n % i == 0)

limit = 20000

map = {n: properDivsSum(n) for n in range(1, limit + 1)}

for n in range(1, limit + 1):
    m = map[n]
    if m > n and m <= limit and map.get(m) == n:
        print(f"{n} {m}")
```