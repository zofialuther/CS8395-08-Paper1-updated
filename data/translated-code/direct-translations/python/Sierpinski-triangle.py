from functools import reduce
from operator import add

def sierpinski(n):
    def go(xs, i):
        s = ' ' * (2 ** i)
        return concatMap(lambda x: [s + x + s])(xs) + (
            concatMap(lambda x: [x + ' ' + x])(xs)
        )
    return '\n'.join(reduce(go, range(n), '*'))

def concatMap(f):
    return lambda xs: (
        reduce(add, map(f, xs), [])
    )

print(sierpinski(4))