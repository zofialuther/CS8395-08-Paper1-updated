def floyd(n):
    return take(n)(iterate(nextFloyd)([1]))


def nextFloyd(xs):
    n = succ(len(xs))
    if n < 2:
        return [1]
    else:
        return enumFromTo(succ(n * pred(n) // 2))(n * succ(n) // 2)


def showFloyd(xs):
    return unlines(map(str, xs))


def main():
    print(showFloyd(floyd(5)))


def enumFromTo(m):
    return lambda n: list(range(m, n + 1))


def iterate(f):
    def inner(x):
        v = x
        while True:
            yield v
            v = f(v)
    return inner


def pred(x):
    if isinstance(x, int):
        return x - 1
    else:
        return chr(ord(x) - 1)


def succ(x):
    if isinstance(x, int):
        return x + 1
    else:
        return chr(ord(x) + 1)


def take(n):
    def inner(xs):
        if isinstance(xs, list):
            return xs[0:n]
        else:
            return islice(xs, n)
    return inner


def unlines(xs):
    return '\n'.join(xs)


if __name__ == '__main__':
    main()