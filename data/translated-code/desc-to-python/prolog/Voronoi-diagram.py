```python
import random
import math
import pygame

def distance(p1, p2, method):
    if method == "Manhattan":
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    elif method == "Euclidean":
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    elif method == "Minkowski":
        return (abs(p1[0] - p2[0])**3 + abs(p1[1] - p2[1])**3)**(1/3)

def voronoi(V, method):
    width, height = 400, 400
    win = pygame.display.set_mode((width, height))
    image = pygame.Surface((width, height))
    sites = [(random.randint(0, width), random.randint(0, height)) for _ in range(V)]
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(V)]

    for x in range(width):
        for y in range(height):
            distances = [distance((x, y), site, method) for site in sites]
            min_distance = min(distances)
            min_index = distances.index(min_distance)
            image.set_at((x, y), colors[min_index])
    
    win.blit(image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

voronoi(10, "Manhattan")
voronoi(10, "Euclidean")
voronoi(10, "Minkowski")
```