def floyd_warshall(graph):
    distance = [[float('inf') if i != j else 0 for j in range(len(graph))] for i in range(len(graph)]
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance