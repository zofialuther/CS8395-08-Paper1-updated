```python
import math

IMAGE_SIZE = 700
SIN_60_DEGREES = math.sin(math.pi / 3.0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main(aArgs):
    points = initialEquilateralTriangle()
    for i in range(4):
        points = nextIteration(points)
    text = kochCurveText(points, IMAGE_SIZE)
    writeToFile(text)

def initialEquilateralTriangle():
    margin = 50
    boxSize = IMAGE_SIZE - margin
    sideLength = round(boxSize * SIN_60_DEGREES)
    x = (boxSize + margin - sideLength) / 2
    y = round((boxSize + margin) / 2 - sideLength * SIN_60_DEGREES / 3)
    points = [
        Point(x, y),
        Point(x + sideLength / 2, y + sideLength * SIN_60_DEGREES),
        Point(x + sideLength, y),
        Point(x, y)
    ]
    return points

def nextIteration(aPoints):
    result = []
    for i in range(len(aPoints) - 1):
        x0 = aPoints[i].x
        y0 = aPoints[i].y
        x1 = aPoints[i + 1].x
        y1 = aPoints[i + 1].y
        dy = y1 - y0
        dx = x1 - x0
        result.append(aPoints[i])
        result.append(Point(x0 + dx / 3, y0 + dy / 3))
        result.append(Point(round(x0 + dx / 2 - dy * SIN_60_DEGREES / 3), round(y0 + dy / 2 + dx * SIN_60_DEGREES / 3)))
        result.append(Point(x0 + 2 * dx / 3, y0 + 2 * dy / 3))
    result.append(aPoints[len(aPoints) - 1])
    return result

def kochCurveText(aPoints, aSize):
    text = "<svg xmlns='http://www.w3.org/2000/svg' width='" + str(aSize) + "' height='" + str(aSize) + "'>\n"
    text += "<rect style='width:100%;height:100%;fill:cyan'/>\n"
    text += "<polygon points='"
    for i in range(len(aPoints)):
        text += str(aPoints[i].x) + ", " + str(aPoints[i].y) + " "
    text += "' style='fill:pink;stroke:black;stroke-width:2'/>\n</svg>\n"
    return text
```