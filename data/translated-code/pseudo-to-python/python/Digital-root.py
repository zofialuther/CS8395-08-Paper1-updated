```python
from functools import reduce

# main :: IO ()
def main():
    print(
        tabulated(digitalRoot)(
            'Integer -> (additive persistence, digital root):'
        )([627615, 39390, 588225, 393900588225, 55])
    )


# digitalRoot :: Int -> (Int, Int)
def digitalRoot(n):
    '''Integer -> (additive persistence, digital root)'''
    def f(pn):
        p, n = pn
        return (
            1 + p,
            reduce(lambda a, x: a + int(x), str(n), 0)
        )

    def p(pn):
        return 10 > pn[1]

    return until(p)(f)(
        (0, abs(int(n)))
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    return lambda f: lambda x: g(f(x))


# tabulated :: (a -> b) -> String -> String
def tabulated(f):
    def go(s, xs):
        fw = compose(len)(str)
        w = fw(max(xs, key=fw))
        return s + '\n' + '\n'.join(list(map(
            lambda x: str(x).rjust(w, ' ') + ' -> ' + str(f(x)), xs
        )))

    return lambda s: lambda xs: go(s, xs)


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v

    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()
```