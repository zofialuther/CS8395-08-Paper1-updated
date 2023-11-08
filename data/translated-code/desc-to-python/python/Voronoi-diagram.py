import numpy as np
from PIL import Image
from scipy.spatial import Voronoi, voronoi_plot_2d, KDTree

# Create random colors and points
colors = np.random.rand(10, 3)
points = np.random.rand(10, 2)

# Construct a list of all possible (y,x) coordinates
coordinates = np.array([[y, x] for y in range(512) for x in range(512)])

# Find the closest point to each coordinate using KDTree
tree = KDTree(points)
closest_point_indices = tree.query(coordinates)[1]
closest_colors = colors[closest_point_indices]

# Create an image with the corresponding color for each point
image = Image.new('RGB', (512, 512))
image.putdata(closest_colors)

# Export the diagram as an RGB image in a PNG format
image.save('voronoi_diagram.png', 'PNG')

# Display the diagram
image.show()