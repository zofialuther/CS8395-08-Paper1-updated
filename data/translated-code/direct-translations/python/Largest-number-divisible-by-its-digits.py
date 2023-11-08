from itertools import chain, permutations
from functools import reduce
from math import gcd


def main():
    digits = [1, 2, 3, 4, 6, 7, 8, 9]
    lcmDigits = reduce(lcm, digits)
    sevenDigits = (delete(digits)(x) for x in [1, 4, 7])

    print(
        max(
            (
                intFromDigits(x) for x
                in concatMap(permutations)(sevenDigits)
            ),
            key=lambda n: n if 0 == n % lcmDigits else 0
        )
    )


def intFromDigits(xs):
    return reduce(lambda a, x: a * 10 + x, xs, 0)


def concatMap(f):
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


def delete(xs):
    def go(x):
        ys = xs.copy()
        ys.remove(x)
        return ys
    return go


def lcm(x, y):
    return 0 if (0 == x or 0 == y) else abs(
        y * (x // gcd(x, y))
    )


if __name__ == '__main__':
    main()