from functools import reduce
from itertools import chain

# modInv :: Int -> Int -> Maybe Int
def modInv(a):
    return lambda m: (
        lambda ig=gcdExt(a)(m): (
            lambda i=ig[0]: (
                Just(i + m) if i < 0 else Just(i) if ig[2] == 1 else Nothing()
            )
        )()
    )()

# gcdExt :: Int -> Int -> (Int, Int, Int)
def gcdExt(x):
    def go(a, b):
        if b == 0:
            return (1, 0, a)
        else:
            q, r = divmod(a, b)
            s, t, g = go(b, r)
            return (t, s - q * t, g)
    return lambda y: go(x, y)

#  TEST ---------------------------------------------------

# Numbers between 2010 and 2015 which do yield modular inverses for 42:

# main :: IO ()
def main():
    print(
        mapMaybe(
            lambda y: bindMay(modInv(42)(y))(
                lambda mInv: Just((y, mInv))
            )
        )(
            enumFromTo(2010)(2025)
        )
    )

# GENERIC ABSTRACTIONS ------------------------------------

# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    return lambda n: list(range(m, n + 1))

# bindMay (>>=) :: Maybe  a -> (a -> Maybe b) -> Maybe b
def bindMay(m):
    return lambda mf: m if m['Nothing'] else mf(m['Just'])

# Just :: a -> Maybe a
def Just(x):
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}

# mapMaybe :: (a -> Maybe b) -> [a] -> [b]
def mapMaybe(mf):
    return lambda xs: reduce(
        lambda a, x: a + [x] if x is not None else a,
        map(mf, xs),
        []
    )

# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    return lambda f: lambda m: v if m['Nothing'] else f(m['Just'])

# Nothing :: Maybe a
def Nothing():
    return {'type': 'Maybe', 'Nothing': True}

# MAIN ---
main()