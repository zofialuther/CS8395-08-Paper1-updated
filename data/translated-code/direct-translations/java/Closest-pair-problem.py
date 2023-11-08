```python
import random

class ClosestPair:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return "(" + str(self.x) + ", " + str(self.y) + ")"

    class Pair:
        def __init__(self, point1=None, point2=None):
            self.point1 = point1
            self.point2 = point2
            self.distance = 0.0
            if point1 and point2:
                self.calcDistance()

        def update(self, point1, point2, distance):
            self.point1 = point1
            self.point2 = point2
            self.distance = distance

        def calcDistance(self):
            self.distance = self.distance(self.point1, self.point2)

        def __str__(self):
            return str(self.point1) + "-" + str(self.point2) + " : " + str(self.distance)

    @staticmethod
    def distance(p1, p2):
        xdist = p2.x - p1.x
        ydist = p2.y - p1.y
        return ((xdist ** 2) + (ydist ** 2)) ** 0.5

    @staticmethod
    def bruteForce(points):
        numPoints = len(points)
        if numPoints < 2:
            return None
        pair = ClosestPair.Pair(points[0], points[1])
        if numPoints > 2:
            for i in range(numPoints - 1):
                point1 = points[i]
                for j in range(i + 1, numPoints):
                    point2 = points[j]
                    distance = ClosestPair.distance(point1, point2)
                    if distance < pair.distance:
                        pair.update(point1, point2, distance)
        return pair

    @staticmethod
    def sortByX(points):
        points.sort(key=lambda point: point.x)

    @staticmethod
    def sortByY(points):
        points.sort(key=lambda point: point.y)

    @staticmethod
    def divideAndConquer(points):
        pointsSortedByX = points.copy()
        ClosestPair.sortByX(pointsSortedByX)
        pointsSortedByY = points.copy()
        ClosestPair.sortByY(pointsSortedByY)
        return ClosestPair.divideAndConquer(pointsSortedByX, pointsSortedByY)

    @staticmethod
    def divideAndConquer(pointsSortedByX, pointsSortedByY):
        numPoints = len(pointsSortedByX)
        if numPoints <= 3:
            return ClosestPair.bruteForce(pointsSortedByX)

        dividingIndex = numPoints // 2
        leftOfCenter = pointsSortedByX[:dividingIndex]
        rightOfCenter = pointsSortedByX[dividingIndex:]

        tempList = leftOfCenter.copy()
        ClosestPair.sortByY(tempList)
        closestPair = ClosestPair.divideAndConquer(leftOfCenter, tempList)

        tempList.clear()
        tempList.extend(rightOfCenter)
        ClosestPair.sortByY(tempList)
        closestPairRight = ClosestPair.divideAndConquer(rightOfCenter, tempList)

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
                distance = ClosestPair.distance(point1, point2)
                if distance < closestPair.distance:
                    closestPair.update(point1, point2, distance)
                    shortestDistance = distance
        return closestPair

    @staticmethod
    def main(args):
        numPoints = int(args[0]) if args else 1000
        points = [ClosestPair.Point(random.random(), random.random()) for _ in range(numPoints)]
        print("Generated " + str(numPoints) + " random points")
        startTime = int(round(time.time() * 1000))
        bruteForceClosestPair = ClosestPair.bruteForce(points)
        elapsedTime = int(round(time.time() * 1000)) - startTime
        print("Brute force (" + str(elapsedTime) + " ms): " + str(bruteForceClosestPair))
        startTime = int(round(time.time() * 1000))
        dqClosestPair = ClosestPair.divideAndConquer(points)
        elapsedTime = int(round(time.time() * 1000)) - startTime
        print("Divide and conquer (" + str(elapsedTime) + " ms): " + str(dqClosestPair))
        if bruteForceClosestPair.distance != dqClosestPair.distance:
            print("MISMATCH")

if __name__ == "__main__":
    import sys
    import time
    ClosestPair.main(sys.argv[1:])
```