import pygame
import math

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal Tree")

# Define the drawTree function
def drawTree(x, y, length, angle, depth):
    if depth > 0:
        x2 = x + int(math.cos(math.radians(angle)) * length * depth)
        y2 = y - int(math.sin(math.radians(angle)) * length * depth)
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x2, y2), 2)
        drawTree(x2, y2, length, angle - 20, depth - 1)
        drawTree(x2, y2, length, angle + 20, depth - 1)

# Handle the event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the fractal tree
    drawTree(400, 600, 50, -90, 9)
    pygame.display.flip()

# Quit the program
pygame.quit()