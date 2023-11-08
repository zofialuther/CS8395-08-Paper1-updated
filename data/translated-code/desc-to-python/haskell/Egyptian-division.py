```python
from itertools import accumulate

def egyptianQuotRem(dividend, divisor):
    def unfoldr(f, x):
        while True:
            x = f(x)
            yield x[0]
            if not x[1]:
                break
    
    def doubleRow(acc, x):
        if acc[-1] + x <= dividend:
            return (acc + [acc[-1] + x], x * 2)
        else:
            return (acc, 0)
    
    rows = list(unfoldr(lambda x: doubleRow(x, divisor), [divisor]))
    quot = len(rows)
    remainder = dividend - list(accumulate(rows))[-2]
    return (quot, remainder)

inputs = (25, 3)
result = egyptianQuotRem(*inputs)
print(result)
```