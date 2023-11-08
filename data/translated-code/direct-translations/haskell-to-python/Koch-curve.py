from math import cos, sin, pi
from Data.Bifunctor import bimap
from Text.Printf import printf

def kochSnowflake(n, a, b):
    points = [a, equilateralApex(a, b), b]
    return sum([kochCurve(n, p1, p2) for p1, p2 in zip(points, points[1:] + [points[0]])], [])

def kochCurve(n, ab, xy):
    return [ab] + go(n, (ab, xy))

def go(n, ab_xy):
    ab, xy = ab_xy
    if n == 0:
        return [xy]
    else:
        mp, mq = midThirdOfLine(ab, xy)
        points = [ab, mp, equilateralApex(mp, mq), mq, xy]
        return go(n-1, (p1, p2) for p1, p2 in zip(points, points[1:]))

def equilateralApex(a, b):
    return rotatedPoint(pi / 3, a, b)

def rotatedPoint(theta, ox_oy, a_b):
    ox, oy = ox_oy
    return (ox + dx, oy - dy)
    dx, dy = rotatedVector(theta, (a - ox, oy - b))

def rotatedVector(angle, xy):
    x, y = xy
    return (x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle))

def midThirdOfLine(ab, xy):
    a, b = ab
    x, y = xy
    dx = (x - a) / 3
    dy = (y - b) / 3
    f = bimap(dx.__add__, dy.__add__)
    p = f(a, b)
    return p, f(p)

def main():
    print(svgFromPoints(1024, kochSnowflake(4, (200, 600), (800, 600))))

def svgFromPoints(w, xys):
    sw = str(w)
    showN = lambda x: printf("%.2g", x)
    points = ' '.join([showN(x) + ' ' + showN(y) for x, y in xys])
    return ("\n".join([
        "<svg xmlns=\"http://www.w3.org/2000/svg\"",
        "width=\"512\" height=\"512\" viewBox=\"5 5 " + sw + " " + sw + "\">",
        "<path d=\"M" + points + "\" ",
        "stroke-width=\"2\" stroke=\"red\" fill=\"transparent\"/>",
        "</svg>"
    ]))

main()