```python
import Data.Map as Map

def makeMap(ks, vs):
    return Map.fromList(zip(ks, vs))

mymap = makeMap(['a', 'b', 'c'], [1, 2, 3])
```