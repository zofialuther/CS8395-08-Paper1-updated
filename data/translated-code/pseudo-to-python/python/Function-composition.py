import math

def compose(g, f):
    return lambda x: g(f(x))

def main():
    print(list(map(lambda f: f(0.5),
        zipWith(compose)([math.sin, math.cos, lambda x: x ** 3.0])
            ([math.asin, math.acos, lambda x: x ** (1 / 3.0)])))

def zipWith(f):
    return lambda xs: lambda ys: list(map(f, xs, ys))

if __name__ == '__main__':
    main()