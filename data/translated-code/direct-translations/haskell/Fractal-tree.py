from Graphics.HGL import Window, Run
from Control.Arrow
from Control.Monad
from Data.List
import math

def enumBase(n):
    def repeat(m):
        return [0] * m
    return [list(range(0, m)) for m in repeat(n)]

def psPlus(a, b, p, q):
    return (a + p, b + q)

def toInt(d):
    return int(round(d))

def intPoint(d1, d2):
    return (toInt(d1), toInt(d2))

def pts(n):
    r, h, sr, sh = 50, math.pi / 5, 0.9, 0.75
    rs = [r * (sr ** i) for i in range(n)]
    lhs = [[(-1) ** i for i in range(2)] for _ in range(n)]
    rhs = [h * (sh ** i) for i in range(n)]
    hs = [list(map(sum, zip(map(lambda x: x * r, rs), rhs))] for rs in lhs]

    def calculate_points(hs):
        result = []
        for i in range(n):
            if i == 0:
                result.append(intPoint(100, 300))
            else:
                points = [(h * math.cos(a), h * math.sin(a)) for h, a in zip(rs, hs[i])]
                points = list(map(lambda x: psPlus(100, 0, x[0], x[1]), points))
                points = list(map(intPoint, *zip(*points)))
                points = list(map(lambda x: psPlus(0, 300, x[0], x[1]), points))
                result.append(points)
        return result

    return calculate_points(hs)

def fractalTree(n):
    w = Window("Fractal Tree", (500, 600))
    w.run(setGraphic(w, overGraphics(map(polyline, pts(n - 1)))), getKey(w))

def main():
    fractalTree(10)

main()