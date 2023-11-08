```python
import Data.List
import Data.Ord

wds = ['apple', 'banana', 'orange', 'strawberry', 'pineapple']

def main():
    print(maximumBy(comparing(len), wds))
```