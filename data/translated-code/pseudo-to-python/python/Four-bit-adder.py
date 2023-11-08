def xor(a, b):
    return (a and (not b)) or (b and (not a))

def ha(a, b):
    return xor(a, b), a and b      # sum, carry

def fa(a, b, ci):
    s0, c0 = ha(ci, a)
    s1, c1 = ha(s0, b)
    return s1, c0 or c1      # sum, carry

def fa4(a, b):
    width = 4
    ci = [None] * width
    co = [None] * width
    s  = [None] * width
    for i in range(width):
        if i == 0:
            s[i], co[i] = fa(a[i], b[i], 0)
        else:
            s[i], co[i] = fa(a[i], b[i], co[i-1])
    return s, co[width - 1]

def int2bus(n, width):
    return [int(c) for c in "{0:0{1}b}".format(n, width)[::-1]]

def bus2int(b):
    return sum(1 << i for i, bit in enumerate(b) if bit)

def test_fa4():
    width = 4
    tot = [None] * (width + 1)
    for a in range(2**width):
        for b in range(2**width):
            tot[:width], tot[width] = fa4(int2bus(a, width), int2bus(b, width))
            assert a + b == bus2int(tot), "totals don't match: %i + %i != %s" % (a, b, tot)

if __name__ == '__main__':
    test_fa4()