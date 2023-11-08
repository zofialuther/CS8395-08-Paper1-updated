```python
from functools import reduce
from itertools import chain, takewhile

def drawTree2(blnCompact):
    def go(blnPruned, tree):
        def measured(x):
            s = ' ' + str(x) + ' '
            return len(s), s

        def lmrFromStrings(xs):
            i = len(xs) // 2
            ls, rs = xs[0:i], xs[i:]
            return ls, rs[0], rs[1:]

        def stringsFromLMR(lmr):
            ls, m, rs = lmr
            return ls + [m] + rs

        def fghOverLMR(f, g, h):
            def go(lmr):
                ls, m, rs = lmr
                return (
                    [f(x) for x in ls],
                    g(m),
                    [h(x) for x in rs]
                )
            return lambda lmr: go(lmr)

        def leftPad(n):
            return lambda s: (' ' * n) + s

        def treeFix(l, m, r):
            def cfix(x):
                return lambda xs: x + xs
            return compose(stringsFromLMR)(
                fghOverLMR(cfix(l), cfix(m), cfix(r))
            )

        def lmrBuild(w, f):
            def go(wsTree):
                nChars, x = wsTree['root']
                _x = ('─' * (w - nChars)) + x
                xs = wsTree['nest']
                lng = len(xs)

                def linked(s):
                    c = s[0]
                    t = s[1:]
                    return _x + '┬' + t if '┌' == c else (
                        _x + '┤' + t if '│' == c else (
                            _x + '┼' + t if '├' == c else (
                                _x + '┴' + t
                            )
                        )
                    )

                if 0 == lng:
                    return ([], _x, [])

                elif 1 == lng:
                    def lineLinked(z):
                        return _x + '─' + z
                    rightAligned = leftPad(1 + w)
                    return fghOverLMR(
                        rightAligned,
                        lineLinked,
                        rightAligned
                    )(f(xs[0]))

                else:
                    rightAligned = leftPad(w)
                    lmrs = [f(x) for x in xs]
                    return fghOverLMR(
                        rightAligned,
                        linked,
                        rightAligned
                    )(
                        lmrFromStrings(
                            intercalate([] if blnCompact else ['│'])(
                                [treeFix(' ', '┌', '│')(lmrs[0])] + [
                                    treeFix('│', '├', '│')(x) for x
                                    in lmrs[1:-1]
                                ] + [treeFix('│', '└', ' ')(lmrs[-1])]
                            )
                        )
                    )
            return lambda wsTree: go(wsTree)

        measuredTree = fmapTree(measured)(tree)
        levelWidths = reduce(
            lambda a, xs: a + [max(x[0] for x in xs)],
            levels(measuredTree),
            []
        )
        treeLines = stringsFromLMR(
            foldr(lmrBuild)(None)(levelWidths)(
                measuredTree
            )
        )
        return [
            s for s in treeLines
            if any(c not in '│ ' for c in s)
        ] if (not blnCompact and blnPruned) else treeLines

    return lambda blnPruned: (
        lambda tree: '\n'.join(go(blnPruned, tree))
    )

def main():
    tree1 = Node(1)([
        Node(2)([
            Node(4)([
                Node(7)([])
            ]),
            Node(5)([])
        ]),
        Node(3)([
            Node(6)([
                Node(8)([]),
                Node(9)([])
            ])
        ])
    ])

    tree2 = Node('Alpha')([
        Node('Beta')([
            Node('Epsilon')([]),
            Node('Zeta')([]),
            Node('Eta')([]),
            Node('Theta')([
                Node('Mu')([]),
                Node('Nu')([])
            ])
        ]),
        Node('Gamma')([
            Node('Xi')([Node('Omicron')([])])
        ]),
        Node('Delta')([
            Node('Iota')([]),
            Node('Kappa')([]),
            Node('Lambda')([])
        ])
    ])

    print(
        '\n\n'.join([
            'Fully compacted (parents not all centered):',
            drawTree2(True)(False)(
                tree1
            ),
            'Expanded with vertically centered parents:',
            drawTree2(False)(False)(
                tree2
            ),
            'Centered parents with nodeless lines pruned out:',
            drawTree2(False)(True)(
                tree2
            )
        ])
    )

def Node(v):
    return lambda xs: {'type': 'Tree', 'root': v, 'nest': xs}

def compose(g):
    return lambda f: lambda x: g(f(x))

def concatMap(f):
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )

def fmapTree(f):
    def go(x):
        return Node(f(x['root']))(
            [go(v) for v in x['nest']]
        )
    return lambda tree: go(tree)

def foldr(f):
    def g(x, a):
        return f(a, x)
    return lambda acc: lambda xs: reduce(
        g, xs[::-1], acc
    )

def intercalate(x):
    return lambda xs: x.join(xs) if isinstance(x, str) else list(
        chain.from_iterable(
            reduce(lambda a, v: a + [x, v], xs[1:], [xs[0]])
        )
    ) if xs else []

def iterate(f):
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)

def levels(tree):
    return list(
        map_(map_(root))(
            takewhile(
                bool,
                iterate(concatMap(nest))(
                    [tree]
                )
            )
        )
    )

def map_(f):
    return lambda xs: list(map(f, xs))

def nest(t):
    return t['nest'] if 'nest' in t else None

def root(t):
    return t['root'] if 'root' in t else None

if __name__ == '__main__':
    main()
```