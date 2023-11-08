```python
import math

def leaptext(x, b):
    if b:
        return str(x) + " is a leap year"
    else:
        return str(x) + " is not a leap year"

def isleapsf(j):
    if j % 100 == 0:
        return j % 400 == 0
    else:
        return j % 4 == 0
```