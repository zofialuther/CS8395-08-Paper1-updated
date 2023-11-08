weights = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]
numVertices = 4

def main():
    floydWarshall(weights, numVertices)

def floydWarshall(weights, numVertices):
    dist = [[float('inf')] * numVertices for _ in range(numVertices)]
    for w in weights:
        dist[w[0] - 1][w[1] - 1] = w[2]
    
    next = [[0] * numVertices for _ in range(numVertices)]
    for i in range(numVertices):
        for j in range(numVertices):
            if i != j:
                next[i][j] = j + 1
    
    for k in range(numVertices):
        for i in range(numVertices):
            for j in range(numVertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    printResult(dist, next)

def printResult(dist, next):
    print("pair     dist    path")
    for i in range(len(next)):
        for j in range(len(next)):
            if i != j:
                u = i + 1
                v = j + 1
                path = "{} -> {}    {:2d}     {}".format(u, v, int(dist[i][j]), u)
                while u != v:
                    u = next[u - 1][v - 1]
                    path += " -> " + str(u)
                print(path)