def mulTable(n):
    colWidth = len(str(n * n))
    def pad(s):
        return s.rjust(colWidth, ' ')
    xs = list(range(1, n+1))
    result = []
    for y in xs:
        row = pad(str(y) + ':') + ' '
        for x in xs:
            if x >= y:
                row = row + pad(str(x * y)) + ' '
            else:
                row = row + ''
        result.append(row)
    return '\n'.join(result)

def mulTable2(n):
    colWidth = len(str(n * n))
    def pad(s):
        return s.rjust(colWidth, ' ')
    xs = list(range(1, n+1))
    result = []
    for y in xs:
        row = pad(str(y) + ':') + ' '
        for x in xs:
            temp = []
            if x >= y:
                temp.append(pad(str(x * y)) + ' ')
            else:
                temp.append('')
            row = row + ' '.join(temp)
        result.append(row)
    return '\n'.join(result)

def main():
    for s, f in [('list comprehension', mulTable), ('list monad', mulTable2)]:
        print('By ' + s + ' (' + f.__name__ + '):\n\n' + f(12).strip() + '\n')

def bind(xs):
    return lambda f: list(chain.from_iterable(map(f, xs)))

def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))

def unlines(xs):
    return '\n'.join(xs)

def unwords(xs):
    return ' '.join(xs)

if __name__ == '__main__':
    main()