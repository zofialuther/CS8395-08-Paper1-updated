import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.distance = math.hypot(p2.x - p1.x, p2.y - p1.y)

    def update(self, p1, p2, distance):
        self.p1 = p1
        self.p2 = p2
        self.distance = distance

def distance(p1, p2):
    xdist = p2.x - p1.x
    ydist = p2.y - p1.y
    return math.hypot(xdist, ydist)

def bruteForce(points):
    numPoints = len(points)
    if numPoints < 2:
        return None
    pair = Pair(points[0], points[1])
    if numPoints > 2:
        for i in range(numPoints - 1):
            point1 = points[i]
            for j in range(i + 1, numPoints):
                point2 = points[j]
                dist = distance(point1, point2)
                if dist < pair.distance:
                    pair.update(point1, point2, dist)
    return pair

def sortByX(points):
    points.sort(key=lambda p: p.x)

def sortByY(points):
    points.sort(key=lambda p: p.y)

def divideAndConquer(points):
    pointsSortedByX = points.copy()
    sortByX(pointsSortedByX)
    pointsSortedByY = points.copy()
    sortByY(pointsSortedByY)
    return divideAndConquerRec(pointsSortedByX, pointsSortedByY)

def divideAndConquerRec(pointsSortedByX, pointsSortedByY):
    numPoints = len(pointsSortedByX)
    if numPoints <= 3:
        return bruteForce(pointsSortedByX)

    dividingIndex = numPoints // 2
    leftOfCenter = pointsSortedByX[:dividingIndex]
    rightOfCenter = pointsSortedByX[dividingIndex:]

    tempList = leftOfCenter.copy()
    sortByY(tempList)
    closestPair = divideAndConquerRec(leftOfCenter, tempList)

    tempList.clear()
    tempList.extend(rightOfCenter)
    sortByY(tempList)
    closestPairRight = divideAndConquerRec(rightOfCenter, tempList)

    if closestPairRight.distance < closestPair.distance:
        closestPair = closestPairRight

    tempList.clear()
    shortestDistance = closestPair.distance
    centerX = rightOfCenter[0].x
    for point in pointsSortedByY:
        if abs(centerX - point.x) < shortestDistance:
            tempList.append(point)

    for i in range(len(tempList) - 1):
        point1 = tempList[i]
        for j in range(i + 1, len(tempList)):
            point2 = tempList[j]
            if (point2.y - point1.y) >= shortestDistance:
                break
            dist = distance(point1, point2)
            if dist < closestPair.distance:
                closestPair.update(point1, point2, dist)
                shortestDistance = dist
    return closestPair

def main(args):
    numPoints = 1000 if len(args) == 0 else int(args[0])
    points = [Point(random.random(), random.random()) for _ in range(numPoints)]
    print("Generated " + str(numPoints) + " random points")
    startTime = 0  # Replace with current time in milliseconds
    bruteForceClosestPair = bruteForce(points)
    elapsedTime = 0  # Replace with current time - startTime
    print("Brute force (" + str(elapsedTime) + " ms): " + str(bruteForceClosestPair))
    startTime = 0  # Replace with current time in milliseconds
    dqClosestPair = divideAndConquer(points)
    elapsedTime = 0  # Replace with current time - startTime
    print("Divide and conquer (" + str(elapsedTime) + " ms): " + str(dqClosestPair))
    if bruteForceClosestPair.distance != dqClosestPair.distance:
        print("MISMATCH")