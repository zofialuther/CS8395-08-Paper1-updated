def do_find_closest_points(points):
    closest_points = []
    for i in range(len(points)):
        distances = {}
        for j in range(len(points)):
            if i != j:
                distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
                distances[distance] = (points[i], points[j])
        sorted_distances = sorted(distances.keys())
        closest_points.append(distances[sorted_distances[0]])
        closest_points.append(distances[sorted_distances[1]])
    return closest_points