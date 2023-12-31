def zigzag(n):
    def compare(xy):
        x, y = xy
        return (x + y, -y) if (x + y) % 2 else y
    xs = range(n)
    return {index: n for n, index in enumerate(sorted(((x, y) for x in xs for y in xs), key=compare))}

def printzz(myarray):
    n = int(sqrt(len(myarray)) + 0.5)
    xs = range(n)
    print('\n'.join([''.join("%3i" % myarray[(x, y)] for x in xs) for y in xs]))

printzz(zigzag(6))