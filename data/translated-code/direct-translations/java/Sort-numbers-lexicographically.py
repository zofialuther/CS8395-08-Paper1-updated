```python
from typing import List
from functools import reduce

def lex_order(n: int) -> List[int]:
    first = 1
    last = n
    if n < 1:
        first = n
        last = 1
    return sorted(list(range(first, last + 1)), key=str)

def main():
    print("In lexicographical order:\n")
    ints = [0, 5, 13, 21, -22]
    for n in ints:
        print(f"{n}: {lex_order(n)}")

if __name__ == "__main__":
    main()
```