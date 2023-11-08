```python
from math import comb

def sterling2(n, k):
    if n == 0 and k == 0:
        return 1
    if (n > 0 and k == 0) or (n == 0 and k > 0):
        return 0
    if n == k:
        return 1
    if k > n:
        return 0
    return k * sterling2(n-1, k) + sterling2(n-1, k-1)

print("Stirling numbers of the second kind:")
max_val = 12
print("n/k", end="")
for n in range(max_val + 1):
    print(f"{n:10}", end="")
print()
for n in range(max_val + 1):
    print(f"{n:3}", end="")
    for k in range(n + 1):
        print(f"{sterling2(n, k):10}", end="")
    print()
print("The maximum value of S2(100, k) =")
previous = 0
for k in range(1, 101):
    current = sterling2(100, k)
    if current > previous:
        previous = current
    else:
        print(f"{previous}\n({len(str(previous))} digits, k = {k-1})")
        break
```