```python
from typing import TypeVar, Callable
from typing_extensions import Protocol

A = TypeVar('A')
B = TypeVar('B')

class Logger(Protocol):
    def write(self, message: str) -> None:
        ...

def verbose2(logger: Logger, f: Callable[[A, B], A], x: A, y: B) -> A:
    logger.write(f"Input: {x}, {y}")
    result = f(x, y)
    logger.write(f"Output: {result}")
    return result
```