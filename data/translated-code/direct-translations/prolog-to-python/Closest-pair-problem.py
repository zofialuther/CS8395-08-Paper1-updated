class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def do_find_closest_points(points):
    closest_points = []
    for i, p1 in enumerate(points):
        min_distance = float('inf')
        closest_point = None
        for j, p2 in enumerate(points):
            if i != j:
                distance = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    closest_point = p2
        closest_points.append((p1, closest_point))
    return closest_points

points = [
    Point(0.654682, 0.925557),
    Point(0.409382, 0.619391),
    Point(0.891663, 0.888594),
    Point(0.716629, 0.996200),
    Point(0.477721, 0.946355),
    Point(0.925092, 0.818220),
    Point(0.624291, 0.142924),
    Point(0.211332, 0.221507),
    Point(0.293786, 0.691701),
    Point(0.839186, 0.728260)
]

result = do_find_closest_points(points)
for p1, p2 in result:
    print(f"Closest point to ({p1.x}, {p1.y}) is ({p2.x}, {p2.y})")