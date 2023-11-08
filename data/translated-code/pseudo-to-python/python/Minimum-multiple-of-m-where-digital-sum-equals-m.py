```python
from itertools import count, islice

def a131382():
    return (elemIndex(x)(productDigitSums(x)) for x in count(1))

def productDigitSums(n):
    return (digitSum(n * x) for x in count(0))

def main():
    print(table(10)([str(x) for x in islice(a131382(), 40)]))

def chunksOf(n):
    def go(xs):
        return (xs[i:n + i] for i in range(0, len(xs), n)) if 0 < n else None
    return go

def digitSum(n):
    return sum(int(x) for x in list(str(n)))

def elemIndex(x):
    def go(xs):
        try:
            return next(i for i, v in enumerate(xs) if x == v)
        except StopIteration:
            return None
    return go

def table(n):
    def go(xs):
        w = len(xs[-1])
        return '\n'.join(' '.join(row) for row in chunksOf(n)([s.rjust(w, ' ') for s in xs]))
    return go

if __name__ == '__main__':
    main()
```