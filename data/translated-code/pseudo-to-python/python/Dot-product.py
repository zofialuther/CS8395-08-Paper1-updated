def dotProduct(xs):
    def ys(ys):
        if len(xs) != len(ys):
            return Left('vector sizes differ')
        else:
            return Right(sum(map(lambda x, y: x * y, xs, ys))
    return ys

def main():
    print fTable(main.__doc__ + ':\n')(str)(str)(compose(either(append('Undefined :: '))(str))(dotProduct([1, 3, -5])))([[4, -2, -1, 8], [4, -2], [4, 2, -1], [4, -2, -1]])

def Left(x):
    return {'type': 'Either', 'Right': None, 'Left': x}

def Right(x):
    return {'type': 'Either', 'Left': None, 'Right': x}

def append(xs):
    return lambda ys: xs + ys

def compose(g):
    return lambda f: lambda x: g(f(x))

def either(fl, fr, e):
    if e['Right'] is None:
        return fl(e['Left'])
    else:
        return fr(e['Right'])

def fTable(s):
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(xShow, fxShow, f, xs)

if __name__ == '__main__':
    main()