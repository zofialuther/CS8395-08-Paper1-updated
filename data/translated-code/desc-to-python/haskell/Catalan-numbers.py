```python
from itertools import count, accumulate

cats1 = (i * (i + 1) // 2 for i in count(1))
cats2 = (sum(cats2[:i]) for i in count(1))
cats3 = accumulate(count(1), lambda x, _: x * 2)

def main():
    print(list(next(cats1) for _ in range(15)))
    print(list(next(cats2) for _ in range(15)))
    print(list(next(cats3) for _ in range(15)))

main()
```