```python
import random
from enum import Enum

class DutchNationalFlag:
    class DutchColors(Enum):
        RED = 1
        WHITE = 2
        BLUE = 3

    def main(self):
        balls = [0] * 12
        values = list(DutchNationalFlag.DutchColors)
        rand = random.Random()
        for i in range(len(balls)):
            balls[i] = rand.choice(values)
        print("Array before sorting:", balls)
        balls.sort()
        print("Array after sorting:", balls)
        sorted = True
        for i in range(len(balls) - 1):
            if balls[i] > balls[i+1]:
                sorted = False
                break
        if sorted:
            print("Array is correctly sorted")
        else:
            print("Array is not correctly sorted")
```