from enum import Enum
import random

class DutchColors(Enum):
    RED = 1
    WHITE = 2
    BLUE = 3

array = [random.choice(list(DutchColors)) for _ in range(12)]
array.sort()
print(array)