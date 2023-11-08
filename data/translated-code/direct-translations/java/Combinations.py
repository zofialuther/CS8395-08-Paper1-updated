```python
def bitprint(u):
    s = ""
    n = 0
    while u > 0:
        if (u & 1) > 0:
            s += str(n) + " "
        n += 1
        u >>= 1
    return s

def bitcount(u):
    n = 0
    while u > 0:
        n += 1
        u &= (u - 1)
    return n

def comb(c, n):
    s = []
    for u in range(1 << n):
        if bitcount(u) == c:
            s.append(bitprint(u))
    s.sort()
    return s

print(comb(3, 5))
```