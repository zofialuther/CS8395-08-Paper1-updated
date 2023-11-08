'''
Determine if a string has all unique characters
'''

# duplicatedCharIndices :: String -> Maybe (Char, [Int])
def duplicatedCharIndices(s):
    def go(xs):
        if len(xs) > 1:
            duplicates = [
                (k, list(v)) for k, v in groupby(
                    sorted(xs, key=lambda x: x[1]),
                    key=lambda x: x[0]
                ) if len(list(v)) > 1
            ]
            return (duplicates[0][0], duplicates[0][1]) if duplicates else None
        else:
            return None
    return go(list(enumerate(s)))


# main :: IO ()
def main():
    def showSample(s):
        return repr(s) + ' (' + str(len(s)) + ')'

    def showDuplicate(cix):
        c, ix = cix
        return repr(c) + (
            ' (' + hex(ord(c)) + ') at ' + repr(ix)
        )

    print(
        fTable('First duplicated character, if any:')(
            showSample
        )(lambda x: showDuplicate(x) if x else 'None')(duplicatedCharIndices)([
            '', '.', 'abcABC', 'XYZ ZYX',
            '1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ'
        ])
    )


# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# Just :: a -> Maybe a
def Just(x):
    return x


# Nothing :: Maybe a
def Nothing():
    return None


# fmap :: (a -> b) -> [a] -> [b]
def fmap(f):
    return lambda xs: [f(x) for x in xs]


# fst :: (a, b) -> a
def fst(tpl):
    return tpl[0]


# head :: [a] -> a
def head(xs):
    return xs[0] if isinstance(xs, list) else next(xs)


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    return lambda f: lambda m: v if m is None else f(m)


# second :: (a -> b) -> ((c, a) -> (c, b))
def second(f):
    return lambda xy: (xy[0], f(xy[1]))


# snd :: (a, b) -> b
def snd(tpl):
    return tpl[1]


# swap :: (a, b) -> (b, a)
def swap(tpl):
    return (tpl[1], tpl[0])


# MAIN ---
if __name__ == '__main__':
    main()
'''