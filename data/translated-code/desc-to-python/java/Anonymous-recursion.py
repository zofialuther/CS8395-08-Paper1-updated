```python
from typing import Callable

class SelfApplicable:
    def apply(self, func: Callable) -> Callable:
        pass

class Utils:
    @staticmethod
    def y(f: Callable) -> Callable:
        pass

    @staticmethod
    def fix(f: Callable) -> Callable:
        pass

    @staticmethod
    def fib(n: int) -> int:
        pass
```