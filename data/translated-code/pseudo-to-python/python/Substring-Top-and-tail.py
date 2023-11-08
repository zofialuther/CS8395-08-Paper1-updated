```python
def main():
    for xs in transpose(chunksOf(3)(ap([tail, init, compose(init)(tail)])(['knights', 'socks', 'brooms']))):
        print(xs)

def tail(xs):
    return xs[1:]

def init(xs):
    return xs[:-1]

def ap(fs):
    return lambda xs: reduce(lambda a, f: a + reduce(lambda a, x: a + [f(x)], xs, []), fs, [])

def chunksOf(n):
    return lambda xs: reduce(lambda a, i: a + [xs[i:n + i]], range(0, len(xs), n), []) if 0 < n else []

def compose(g):
    return lambda f: lambda x: g(f(x))

def transpose(xs):
    return list(map(list, zip(*xs)))

if __name__ == '__main__':
    main()
```