def kochSnowflake(n, a, b):
    points = [a, equilateralApex(a, b), b]
    return list(chain.from_iterable(map(
        kochCurve(n),
        points,
        points[1:] + [points[0]]
    )))

def kochCurve(n):
    def go(ab, xy):
        return [ab] + koch(n)((ab, xy))
    return go

def equilateralApex(p, q):
    return rotatedPoint(pi / 3)(p, q)

def rotatedPoint(theta):
    def go(xy, ab):
        ox, oy = xy
        a, b = ab
        dx, dy = rotatedVector(theta, (a - ox, oy - b))
        return ox + dx, oy - dy
    return go

def rotatedVector(theta, xy):
    x, y = xy
    return (
        x * cos(theta) - y * sin(theta),
        x * sin(theta) + y * cos(theta)
    )

def midThirdOfLine(ab, xy):
    vector = [x / 3 for x in map(sub, xy, ab)]

    def f(p):
        return tuple(map(add, vector, p))
    p = f(ab)
    return (p, f(p))

def main():
    print(
        svgFromPoints(1024)(
            kochSnowflake(
                4, (200, 600), (800, 600)
            )
        )
    )

def svgFromPoints(w):
    def go(xys):
        xs = ' '.join(map(
            lambda xy: str(round(xy[0], 2)) + ' ' + str(round(xy[1], 2)),
            xys
        ))
        return '\n'.join([
            '<svg xmlns="http://www.w3.org/2000/svg"',
            f'width="512" height="512" viewBox="5 5 {w} {w}">',
            f'<path d="M{xs}" ',
            'stroke-width="2" stroke="red" fill="transparent"/>',
            '</svg>'
        ])
    return go