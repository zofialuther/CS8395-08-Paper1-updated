```python
def floydWarshall(v, dist):
    for k in v:
        new_dist = {}
        for i in v:
            for j in v:
                a = dist.get((i, k))
                b = dist.get((k, j))
                if a is not None and b is not None:
                    new_dist[(i, j)] = (Shortest(a[0] + b[0], a[1]))
        dist.update(new_dist)
```