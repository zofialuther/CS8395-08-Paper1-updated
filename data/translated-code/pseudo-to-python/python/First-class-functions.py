def main():
    pwr = flip(curry(pow))
    fs = [math.sin, math.cos, pwr(3.0)]
    ifs = [math.asin, math.acos, pwr(1 / 3.0)]
    print([f(0.5) for f in zipWith(compose)(fs)(ifs)])

def compose(g):
    return lambda f: lambda x: g(f(x))

def curry(f):
    return lambda a: lambda b: f(a, b)

def flip(f):
    if len(inspect.signature(f).parameters) > 1:
        return lambda a, b: f(b, a)
    else:
        return lambda a: lambda b: f(b)(a)

def zipWith(f):
    return lambda xs: lambda ys: [f(a)(b) for (a, b) in zip(xs, ys)]

if __name__ == '__main__':
    main()