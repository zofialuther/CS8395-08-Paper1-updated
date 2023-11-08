```python
from itertools import islice
from functools import reduce

def longest_common(a, b):
    def pair(lst):
        return tuple(lst)

    return max(
        reduce(lambda x, y: x & y, (set(islice(a, i)) & set(islice(b, j)) for i in range(len(a) + 1) for j in range(len(b) + 1)))
        for a, b in [(a, b), (b, a)]
    )

def main():
    print(longest_common("testing123testing", "thisisatest"))

if __name__ == "__main__":
    main()
```