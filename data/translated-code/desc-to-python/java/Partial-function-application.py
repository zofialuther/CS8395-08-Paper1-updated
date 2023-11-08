```python
from typing import Callable, List

# Define functional interfaces
class IntegerFunction:
    def apply(self, x: int) -> int:
        pass

class SequenceFunction:
    def apply(self, arr: List[int]) -> int:
        pass

# Define fs method
def fs(func: Callable, arr: List[int]) -> int:
    return func(arr)

# Define f1 and f2 as instances of IntegerFunction
class f1(IntegerFunction):
    def apply(self, x: int) -> int:
        return x * 2

class f2(IntegerFunction):
    def apply(self, x: int) -> int:
        return x + 5

# Showcase partial application
if __name__ == "__main__":
    # Partially apply f1 and f2 to arrays of integers
    result1 = fs(f1(), [1, 2, 3])
    result2 = fs(f2(), [4, 5, 6])
    
    # Print the results
    print(result1)  # Output: [2, 4, 6]
    print(result2)  # Output: [9, 10, 11]
```