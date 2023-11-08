```python
from itertools import cycle, islice

def repCycles(cs):
    def is_cyclic(s):
        return any(s == ''.join(islice(cycle(s), len(cs))) for _ in range(len(cs)))
    return list(filter(is_cyclic, cs))

def main():
    result = repCycles(["abc", "def", "abcdef"])
    print(result)

def fTable(s, xShow, fxShow, f, xs):
    def rjust(s, n):
        return s.rjust(n)
    max_len = max(map(lambda x: len(str(x)), xs))
    lines = [s] + list(map(lambda x: f"{xShow(x)}\t{fxShow(f(x))}\t{f(x)}", xs))
    result = '\n'.join(lines)
    print(result)

main()
```