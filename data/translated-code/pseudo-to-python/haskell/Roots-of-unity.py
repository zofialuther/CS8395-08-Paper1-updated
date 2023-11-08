```python
from Data.Complex import Complex, cis
from Data.Enum import Enum
from Data.Floating import Floating
from Control.Monad import mapM_

def rootsOfUnity(n: Enum and Floating) -> [Complex]:
    return [cis(2 * pi * k / n) for k in range(0, n)]

def main() -> IO ():
    mapM_(print, rootsOfUnity(3))
```