```python
from abc import ABC, abstractmethod
import math

class FirstClass:
    class Function(ABC):
        @abstractmethod
        def apply(self, x):
            pass

if __name__ == "__main__":
    class TrigFunction(FirstClass.Function):
        def apply(self, x):
            return math.sin(x)
        
    class InverseTrigFunction(FirstClass.Function):
        def apply(self, x):
            return math.asin(x)
        
    trig_functions = [TrigFunction(), TrigFunction(), TrigFunction()]
    inverse_functions = [InverseTrigFunction(), InverseTrigFunction(), InverseTrigFunction()]
    
    for func in trig_functions:
        result = func.apply(0.5)
        print(result)
    
    for func in inverse_functions:
        result = func.apply(0.5)
        print(result)
```