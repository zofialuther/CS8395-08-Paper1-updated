def applyN(n):
    def go(f):
        def inner(x):
            return reduce(lambda a, g: g(a), repeat(f, n), x)
        return inner
    return lambda f: go(f)

def main():
    def f(x):
        return x + 'Example\n'

    def g(x):
        return 2 * x

    def h(x):
        return 1.05 * x

    print(
        fTable(__doc__ + ':')(
            lambda fx: '\nRepeated * 3:\n (' + (
                getsource(fst(fx)).strip() + ')(' +
                repr(snd(fx)) + ')'
            )
        )(str)(
            liftA2(applyN(3))(fst)(snd)
        )([(f, '\n'), (g, 1), (h, 100)])
    )

def compose(g):
    return lambda f: lambda x: g(f(x))

def fst(tpl):
    return tpl[0]

def liftA2(op):
    return lambda f: lambda g: lambda x: op(f(x))(g(x))

def snd(tpl):
    return tpl[1]

def fTable(s):
    return lambda xShow: lambda fxShow: lambda f: lambda xs: 
        ys = list(map(xShow, xs))
        w = max([len(y) for y in ys])
        return s + '\n' + '\n'.join([ys[index].rjust(w, ' ') + ' -> ' + fxShow(f(x)) for index, x in enumerate(xs)])

if __name__ == "__main__":
    main()