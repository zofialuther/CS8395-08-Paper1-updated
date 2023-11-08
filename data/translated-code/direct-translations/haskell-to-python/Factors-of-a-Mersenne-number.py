```python
import Data.List
from HFM.Primes import isPrime
from Control.Monad import liftM2
from Control.Arrow import (uncurry, flip)

def int2bin(x):
    return list(reversed(list(unfoldr(lambda x: (None, None) if x==0 else ((x%2, x//2), x//2), x))))

def trialfac(m):
    qs = [x for x in range(1, m//2+1)]
    qs = list(filter(lambda x: (x%8==1 or x%8==7) and isPrime(x), map(lambda x: 2*m*x+1, qs)))
    bs = int2bin(m)
    def pm(n, b):
        return 2**b*n*n
    return next(filter(lambda q: (lambda q: functools.reduce(lambda a, b: a*(pm(b, x) % q), bs, 1))(q) != 1, qs))
```