```python
from __future__ import print_function
import itertools

def narcissists():
    n = 1
    count = 0
    while count < 25:
        digits = len(str(n))
        total = sum(int(x)**digits for x in str(n))
        if total == n:
            if count % 5 == 0 and count != 0:
                print()
            print(n, end=' ')
            count += 1
        n += 1

narcissists()
```