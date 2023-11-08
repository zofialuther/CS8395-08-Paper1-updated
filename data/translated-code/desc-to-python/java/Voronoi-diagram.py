```python
# Python code to create a Voronoi diagram using random points and colors
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generate random points
points = np.random.rand(10, 2)

# Create Voronoi diagram
vor = Voronoi(points)

# Plot the Voronoi diagram
voronoi_plot_2d(vor)
plt.show()
```