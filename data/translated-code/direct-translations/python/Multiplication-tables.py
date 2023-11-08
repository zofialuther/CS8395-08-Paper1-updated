```python
from itertools import chain

# mulTable :: int -> str
def mulTable(n):
    colWidth = len(str(n * n))

    def pad(s):
        return s.rjust(colWidth, ' ')

    xs = enumFromTo(1)(n)
    return unlines([
        pad(str(y) + ':') + unwords([
            pad(str(x * y) if x >= y else '')
            for x in xs
        ]) for y in xs
    ])

# mulTable2 :: int -> str
def mulTable2(n):
    colWidth = len(str(n * n))

    def pad(s):
        return s.rjust(colWidth, ' ')

    xs = enumFromTo(1)(n)
    return unlines(
        bind(xs)(lambda y: [
            pad(str(y) + ':') + unwords(
                bind(xs)(lambda x: [
                    pad(str(x * y) if x >= y else '')
                ])
            )
        ])
    )

# main :: () -> IO ()
def main():
    for s, f in [
            ('list comprehension', mulTable),
            ('list monad', mulTable2)
    ]:
        print(
            'By ' + s + ' (' + f.__name__ + '):\n\n',
            f(12).strip() + '\n'
        )

# bind (>>=) :: [a] -> (a -> [b]) -> [b]
def bind(xs):
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )

# enumFromTo :: (int, int) -> [int]
def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

# unlines :: [str] -> str
def unlines(xs):
    return '\n'.join(xs)

# unwords :: [str] -> str
def unwords(xs):
    return ' '.join(xs)

if __name__ == '__main__':
    main()
```