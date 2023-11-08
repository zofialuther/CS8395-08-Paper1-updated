```python
primesST = [2, 3]

def sieve(x, q, ps, fs, ft):
    if x >= q:
        return []
    else:
        return [x] + sieve(x+2, q, ps, [p for p in fs if x % p != 0], ft)

primesST = primesST + sieve(5, 9, primesST[1:], primesST[2:])
```