import numpy as np
from PIL import Image
from scipy.spatial import KDTree

def generate_voronoi_diagram(X, Y, num_cells):
    colors = np.random.randint(0, 256, size=(num_cells, 3), dtype=np.uint8)
    points = np.random.rand(num_cells, 2)
    
    idx = np.indices((Y, X))
    coords = np.moveaxis(idx, 0, -1).reshape(-1, 2)
    
    tree = KDTree(points)
    _d, labels = tree.query(coords)
    labels = labels.reshape(Y, X)
    
    rgb = colors[labels]
    img = Image.fromarray(rgb, mode='RGB')
    img.save('VoronoiDiagram.png', format='PNG')
    img.show()
    return rgb