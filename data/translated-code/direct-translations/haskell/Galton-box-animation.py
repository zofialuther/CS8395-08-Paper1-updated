```python
from random import randint
import pygame
import sys

class Ball:
    def __init__(self, position, turns):
        self.position = position
        self.turns = turns

def make_ball(y):
    return Ball((0, y), random_turns())

def random_turns():
    return [randint(-1, 1) for _ in range(5)]

def update_ball(ball, nRows):
    x, y = ball.position
    turns = ball.turns
    if y < -nRows-5:
        return Ball((x + turns[0], y - 1), turns[1:])
    else:
        return Ball((x, y - 1), turns)

def update_world(world):
    nRows, balls, bins = world
    new_balls = [update_ball(ball, nRows) for ball in balls]
    if new_balls[0].position[1] < -nRows-5:
        new_bins = {x: bins.get(x, 0) + 1 for x in range(new_balls[0].position[0], new_balls[0].position[0] + 1)}
    else:
        new_bins = bins
    return nRows, new_balls, new_bins

def draw_world(world):
    nRows, balls, bins = world
    ball_positions = [ball.position for ball in balls if ball.position[1] < 3]
    bin_rects = [draw_bin(x, -nRows-7, h) for x, h in bins.items()]
    pin_positions = [(20 * x, 20 * y) for i in range(1, nRows+1) for j in range(1, i+1) for x, y in [(2*j-i-1, -i-1)]]
    return ball_positions, bin_rects, pin_positions

def draw_bin(x, y, h):
    return (x * 20, -y * 20, 20, -h * 20)

def start_simulation(nRows, balls):
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    world = (nRows, balls, {})
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        ball_positions, bin_rects, pin_positions = draw_world(world)

        for x, y in ball_positions:
            pygame.draw.circle(screen, (255, 0, 0), (x * 20, -y * 20), 10)
        for rect in bin_rects:
            pygame.draw.rect(screen, (0, 0, 0), rect)
        for x, y in pin_positions:
            pygame.draw.circle(screen, (0, 0, 255), (x * 20, -y * 20), 4)

        pygame.display.flip()
        clock.tick(50)

        world = update_world(world)

if __name__ == "__main__":
    start_simulation(10, [make_ball(y) for y in range(1, 11)])
```