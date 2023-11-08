```python
from typing import TypeVar, List
from dataclasses import dataclass
from typing import TypeVar, List

A = TypeVar('A')

@dataclass
class PrintAllType:
    def __init__(self, value: A):
        self.value = value

    def print_all(self, lst: List[A]) -> None:
        mapM_(print, lst)
```