```python
import numpy as np

# Read the file "triangle.txt" and store the triangle as a 2D array
triangle = np.loadtxt("triangle.txt")

# Iterate through the triangle from bottom to top, calculating the maximum path sum at each point
for i in range(len(triangle)-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

# Print the maximum path sum at the top of the triangle
print(triangle[0][0])
```