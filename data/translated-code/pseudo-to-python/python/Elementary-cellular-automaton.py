def eca(cells, rule):
    lencells = len(cells)
    c = "0" + cells + "0"    # Zero pad the ends
    rulebits = format(rule, '08b')
    neighbours2next = {}
    for n in range(8):
        neighbours2next['{0:03b}'.format(n)] = rulebits[::-1][n]
    yield c[1:-1]
    while True:
        c = ''
        for i in range(1, lencells+1):
            c = c + neighbours2next[c[i-1:i+2]]
        c = '0' + c + '0'
        yield c[1:-1]

if __name__ == '__main__':
    lines, start, rules = 50, '0000000001000000000', (90, 30, 122)
    zipped = []
    for rule in rules:
        zipped.append([eca(start, rule) for _ in range(lines)])
    print('\n   Rules: %r' % (rules,))
    for data in zip(*zipped):
        i = data[0]
        cells = data[1:]
        print('%2i: %s' % (i, '    '.join(cells).replace('0', '.').replace('1', '#')))