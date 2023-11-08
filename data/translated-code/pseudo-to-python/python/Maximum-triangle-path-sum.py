```python
import itertools

f = lambda x, y, z: x + max(y, z)
g = lambda xs, ys: [f(x, y, z) for x, y, z in zip(xs, ys, itertools.islice(xs, 1, None))]

with open("triangle.txt", "r") as file:
    data = [list(map(int, line.strip().split())) for line in file]
data.reverse()

print(itertools.reduce(g, data)[0])
```