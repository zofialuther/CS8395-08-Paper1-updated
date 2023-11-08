```python
import itertools

with open("triangle.txt", "r") as file:
    triangle = [[int(num) for num in line.split()] for line in file.readlines()]

f = lambda x, y: x + y
g = lambda x, y: max(x, y)

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += g(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])
```