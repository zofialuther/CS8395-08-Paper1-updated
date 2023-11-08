```python
from functools import partial
from itertools import starmap

def main():
    for n in range(1, 11):
        print(n, end=", " if n < 10 else "\n")

main()
```