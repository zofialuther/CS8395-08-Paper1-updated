```python
import itertools
import operator

def vanEck():
    def go(x, dct, i):
        if x not in dct:
            dct[x] = i
            return (0, dct)
        else:
            return (i - dct[x], dct)

    return list(itertools.accumulate(itertools.count(1), initial=0, func=operator.itemgetter(0)))

def main():
    v = vanEck()
    print(list(itertools.islice(v, 10)))
    print(list(itertools.islice(v, 1000)))
    print(list(itertools.islice(v, 10000)))
    print(list(itertools.islice(v, 100000)))
    print(list(itertools.islice(v, 1000000)))
```