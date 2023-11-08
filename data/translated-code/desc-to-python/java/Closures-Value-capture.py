```python
from typing import List
from java.util.function import IntSupplier
from java.util.stream import IntStream

class ValueCapture:
    @staticmethod
    def main(args: List[str]):
        closures = IntStream.range(1, 6).mapToObj(lambda x: IntSupplier(lambda: x * x)).collect(Collectors.toList())
        specific_closure = closures.get(2)
        print(specific_closure.getAsInt())
```