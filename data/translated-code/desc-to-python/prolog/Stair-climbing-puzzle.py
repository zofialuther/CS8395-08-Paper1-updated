```python
from random import randint

def setup():
    retractall(level(_))
    assertz(level(1))

def step():
    level(X)
    random_num = randint(0, 3)
    if random_num > 0:
        New_Level is X + 1
    else:
        New_Level is X - 1
    retract(level(X))
    assertz(level(New_Level))
    if random_num == 0:
        fail
```