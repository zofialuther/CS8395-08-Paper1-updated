def floydWarshall(v, dist):
    for k in v:
        for i in v:
            for j in v:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist