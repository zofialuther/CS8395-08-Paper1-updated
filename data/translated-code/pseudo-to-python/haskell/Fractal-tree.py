def enumBase(n, m):
    result = []
    for i in range(n):
        sublist = []
        for j in range(m):
            sublist.append(j)
        result.append(sublist)
    return result

def psPlus(a, b, p, q):
    return [a + p, b + q]

def toInt(num):
    return round(num)

def intPoint(a, b):
    return [toInt(a), toInt(b)]

def pts(n):
    r = 50
    h = math.pi / 5
    sr = 0.9
    sh = 0.75
    rs = []
    for i in range(n):
        rs.append(r * math.pow(sr, i))
    lhs = list(map(lambda sublist: list(map(lambda item: math.pow(-1, item), sublist)), enumBase(n, 2)))
    rhs = []
    for i in range(n):
        rhs.append(h * math.pow(sh, i))
    hs = list(map(lambda sublist, index: list(map(lambda item, i: item * rhs[index][i], sublist)), lhs, range(len(lhs))))
    result = []
    for i in range(n):
        sublist = []
        for j in range(n):
            x = (100 if j == 0 else rs[j] * math.cos(hs[j][i]))
            y = (300 if j == 0 else rs[j] * math.sin(hs[j][i]))
            point = intPoint(x, y)
            sublist.append(point)
        result.append(sublist)
    return result

def fractalTree(n):
    window = createWindow("Fractal Tree", 500, 600)
    setGraphic(window, overGraphics(list(map(lambda sublist: polyline(sublist), pts(n - 1)))))
    getKey(window)

fractalTree(10)