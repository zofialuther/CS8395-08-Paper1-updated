```python
from random import randint

# Declare dynamic predicate level/1
level = [1]

# Define setup predicate
def setup():
    level.clear()
    level.append(1)

# Define step predicate
def step():
    Level = level[0]
    N = randint(0,3)
    if N > 0:
        NewLevel = Level + 1
        print(f'Climbed up to {NewLevel}')
    else:
        NewLevel = Level - 1
        print(f'Fell down to {NewLevel}')
    level.clear()
    level.append(NewLevel)
    return N > 0  # Fail if 0 because that is a non step up.
```