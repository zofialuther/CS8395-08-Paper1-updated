```python
from typing import Callable

class Repeat:
    @staticmethod
    def main():
        Repeat.repeat(3, lambda x: print("Example", x))

    @staticmethod
    def repeat(n: int, func: Callable[[int], None]):
        for i in range(n):
            func(i)
```