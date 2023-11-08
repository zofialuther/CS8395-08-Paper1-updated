```python
from math import gcd

# lcm :: Int -> Int -> Int
def lcm(x):
    '''The smallest positive integer divisible
       without remainder by both x and y.
    '''
    return lambda y: 0 if 0 in (x, y) else abs(
        y * (x // gcd(x, y))
    )

# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    print(
        fTable(
            __doc__ + 's of 60 and [12..20]:'
        )(repr)(repr)(
            lcm(60)
        )(enumFromTo(12)(20))
    )

    pairs = [(0, 2), (2, 0), (-6, 14), (12, 18)]
    print(
        fTable(
            '\n\n' + __doc__ + 's of ' + repr(pairs) + ':'
        )(repr)(repr)(
            uncurry(lcm)
        )(pairs)
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple, derived from
       a vanilla or curried function.
    '''
    return lambda xy: f(*xy)


# FORMATTING ----------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN ---
if __name__ == '__main__':
    main()
```