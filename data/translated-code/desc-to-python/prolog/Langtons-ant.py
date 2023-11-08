import pygame
import numpy as np

# initialize window
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Langton\'s Ant')

# initialize variables
ant_position = [250, 250]
ant_direction = 0  # 0 for north, 1 for east, 2 for south, 3 for west
grid = np.zeros((500, 500), dtype=bool)

def go():
    global ant_position, ant_direction, grid

    # implement Langton's Ant rules
    if grid[ant_position[0], ant_position[1]]:
        ant_direction = (ant_direction + 1) % 4
    else:
        ant_direction = (ant_direction - 1) % 4
    grid[ant_position[0], ant_position[1]] = not grid[ant_position[0], ant_position[1]]

    # move the ant
    if ant_direction == 0:
        ant_position[1] -= 1
    elif ant_direction == 1:
        ant_position[0] += 1
    elif ant_direction == 2:
        ant_position[1] += 1
    else:
        ant_position[0] -= 1

    # update the window to display the points
    for i in range(500):
        for j in range(500):
            if grid[i, j]:
                window.set_at((i, j), (0, 0, 0))
            else:
                window.set_at((i, j), (255, 255, 255))
    pygame.display.update()