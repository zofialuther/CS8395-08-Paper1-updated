```python
def levenshtein(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(1, rows):
        dist[i][0] = i
    for j in range(1, cols):
        dist[0][j] = j
    
    for j in range(1, cols):
        for i in range(1, rows):
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1
            dist[i][j] = min(dist[i-1][j] + 1,      # deletion
                             dist[i][j-1] + 1,      # insertion
                             dist[i-1][j-1] + cost) # substitution
    
    return dist[rows-1][cols-1]
```