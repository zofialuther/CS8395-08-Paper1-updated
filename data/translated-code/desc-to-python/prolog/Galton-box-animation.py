```python
# Python code for simulating Galton Box

import pygame
import random

# Create window for Galton Box display
pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Galton Box")

# Initialize pins, tubes, and balls

class Pin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,255,255)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 10, 10))

class Tube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,255,255)
        self.capacity = 10
        self.count = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 50, 100))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,255,255)
        self.radius = 5
        self.vel = 5

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.vel

# Define functions for adding balls and displaying pins and tubes

def add_ball():
    pass

def draw_pins():
    pass

def draw_tubes():
    pass
```