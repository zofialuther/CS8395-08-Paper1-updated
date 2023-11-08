```python
from typing import List
from sympy import primerange

# PRIME PARTITIONS
def partitions(x: int, n: int) -> List[int]:
    if n <= 1:
        return [x] if x in primerange(2, x+1) else []
    else:
        ps = list(primerange(2, x+1))
        return go(ps, x, n)

def go(ps: List[int], x: int, n: int) -> List[int]:
    if n == 1:
        return [x] if x in ps else []
    else:
        def found(p):
            return go([i for i in ps if i != p and i <= x-p], x-p, n-1) + [p]
        return list(filter(None, map(found, ps)))

# TEST
def main():
    def justifyLeft(n: int, c: str, s: str):
        return s.ljust(n, c)

    tests = [
        (99809, 1), (18, 2), (19, 3), (20, 4), (2017, 24),
        *[(22699, i) for i in range(1, 5)], (40355, 3)
    ]

    for x, n in tests:
        xs = partitions(x, n)
        if xs:
            print(justifyLeft(9, ' ', f"{(x, n)} -> {'+'.join(map(str, xs))}"))
        else:
            print(justifyLeft(9, ' ', f"{(x, n)} -> (no solution)"))

main()
```