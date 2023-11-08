```python
from math import factorial
from typing import List


def left_fact(n: int) -> int:
    ans = 0
    for k in range(n):
        ans += factorial(k)
    return ans


if __name__ == "__main__":
    for i in range(11):
        print(f"!{i} = {left_fact(i)}")

    for i in range(20, 111, 10):
        print(f"!{i} = {left_fact(i)}")

    for i in range(1000, 10001, 1000):
        print(f"!{i} has {len(str(left_fact(i)))} digits")
```