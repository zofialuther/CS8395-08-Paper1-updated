```python
from typing import Callable

def accumulator(initial: int) -> Callable[[int], int]:
    state = initial
    def add_and_get(value: int) -> int:
        nonlocal state
        state += value
        return state
    return add_and_get

def main():
    acc1 = accumulator(1)
    acc1(5)
    
    acc2 = accumulator(3)
    acc2(2.3)
    
    print(acc1(0) + acc2(0))

main()
```