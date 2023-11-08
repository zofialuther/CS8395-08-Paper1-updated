```python
import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

class ClosestPair:
    def __init__(self, points):
        self.points = points

    def brute_force_closest_pair(self):
        min_distance = float('inf')
        closest_pair = None
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                distance = math.sqrt((self.points[j].x - self.points[i].x)**2 + (self.points[j].y - self.points[i].y)**2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = Pair(self.points[i], self.points[j], distance)
        return closest_pair

    def closest_pair_recursive(self, points):
        # Divide and conquer algorithm to find the closest pair
        pass

# Main method
if __name__ == "__main__":
    points = [Point(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]
    closest_pair_obj = ClosestPair(points)
    brute_force_result = closest_pair_obj.brute_force_closest_pair()
    print("Brute force result:", brute_force_result.point1.x, brute_force_result.point1.y, brute_force_result.point2.x, brute_force_result.point2.y, brute_force_result.distance)
```