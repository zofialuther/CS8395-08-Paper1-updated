from enum import Enum
import random

class DutchColors(Enum):
    RED = 1
    WHITE = 2
    BLUE = 3

balls = [None] * 12
values = list(DutchColors)

for i in range(len(balls)):
    balls[i] = random.choice(values)
print("Before: " + str(balls))

balls.sort()
print("After:  " + str(balls))

sorted = True
for i in range(1, len(balls)):
    if balls[i-1] > balls[i]:
        sorted = False
        break
print("Correctly sorted: " + str(sorted))