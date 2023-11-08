```python
from itertools import islice


# floyd :: int -> [[int]]
def floyd(n):
    '''n rows of a Floyd triangle.'''
    return take(n)(iterate(nextFloyd)([1]))


# nextFloyd :: [int] -> [int]
def nextFloyd(xs):
    '''A Floyd triangle row derived from
       the preceding row.'''
    n = succ(len(xs))
    return [1] if n < 2 else (
        enumFromTo(succ(n * pred(n) // 2))(
            n * succ(n) // 2
        )
    )


# showFloyd :: [[int]] -> str
def showFloyd(xs):
    '''A stringification of Floyd triangle rows.'''
    return unlines(str(x) for x in xs)


# main :: IO ()
def main():
    '''Test'''
    print(showFloyd(
        floyd(5)
    ))


# GENERIC ABSTRACTIONS ------------------------------------

# enumFromTo :: (int, int) -> [int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated applications of f to x.'''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)


# pred ::  Enum a => a -> a
def pred(x):
    '''The predecessor of a value. For numeric types, (- 1).'''
    return x - 1 if isinstance(x, int) else (
        chr(ord(x) - 1)
    )


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value. For numeric types, (1 +).'''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


# take :: int -> [a] -> [a]
# take :: int -> str -> str
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# unlines :: [str] -> str
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# MAIN ----------------------------------------------------
if __name__ == '__main__':
    main()
```