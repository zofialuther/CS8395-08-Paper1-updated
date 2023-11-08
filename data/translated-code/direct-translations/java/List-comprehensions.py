```python
from itertools import combinations

def run(n):
    return [
        [a, b, c]
        for a in range(1, n)
        for b in range(a, n)
        for c in range(b, n)
        if a*a + b*b == c*c
    ]

if __name__ == "__main__":
    print(run(20))
```