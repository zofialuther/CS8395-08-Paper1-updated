def kochSnowflake(n, a, b):
    points = [a, equilateralApex(a, b), b]
    x = points[0]
    xs = points[1:]
    result = []
    for i in range(len(points) - 1):
        result.append(kochCurve(n, points[i], points[i + 1]))
    return result

def kochCurve(n, ab, xy):
    result = [ab]
    result.extend(go(n, (ab, xy)))
    return result

def go(n, abxy):
    ab = abxy[0]
    xy = abxy[1]
    if n == 0:
        return [xy]
    else:
        mpq = midThirdOfLine(ab[0], ab[1], xy[0], xy[1])
        points = [ab, mpq[0], equilateralApex(mpq[0], mpq[1]), mpq[1], xy]
        result = []
        for i in range(len(points) - 1):
            result.append(go(n-1, (points[i], points[i+1])))
        return result

def equilateralApex(a, b):
    return rotatedPoint(3.14/3, a, b)

def rotatedPoint(theta, ox, oy, a, b):
    dx = a - ox
    dy = oy - b
    rotated = rotatedVector(3.14/3, dx, dy)
    return (ox + rotated[0], oy - rotated[1])

def rotatedVector(angle, x, y):
    return (x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle))

def midThirdOfLine(a, b, x, y):
    dx = (x - a) / 3
    dy = (y - b) / 3
    f = lambda dx, dy: (a + dx, b + dy)
    p = f(dx, dy)
    return (p, f(p)) 

def main():
    print(svgFromPoints(1024, kochSnowflake(4, (200, 600), (800, 600)))

def svgFromPoints(w, xys):
    sw = str(w)
    result = "<svg xmlns=\"http://www.w3.org/2000/svg\"\n"
    result += "width=\"512\" height=\"512\" viewBox=\"5 5 " + sw + " " + sw + "\"> \n"
    result += "<path d=\"M"
    for point in xys:
        result += str(point[0]) + " " + str(point[1]) + " "
    result += "\" stroke-width=\"2\" stroke=\"red\" fill=\"transparent\"/>\n"
    result += "</svg>"
    return result