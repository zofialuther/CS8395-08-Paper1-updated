```python
from typing import TypeVar, IO

a = TypeVar('a')
b = TypeVar('b')

class PrintAllType:
    def process(self, a) -> b:
        pass

instance a ~ () => PrintAllType[(IO[a], IO[()])] where
    def process(args):
        mapM_(putStrLn, args)
```