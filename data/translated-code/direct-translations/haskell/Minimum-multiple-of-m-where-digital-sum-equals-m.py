```python
from itertools import count
from functools import reduce
from operator import mul
from math import prod

def productDigitSums(n):
    return sum(map(int, str(prod(range(1, n+1)))))

a131382 = [productDigitSums(n) for n in count(1)]

def table(gap, rows):
    col_widths = [max(map(len, col)) for col in zip(*rows)]
    format_str = ' '.join(['{:' + str(width) + 's}' for width in col_widths])
    return '\n'.join(gap.join(format_str.format(*row) for row in rows))

print(table(" ", [list(map(str, a131382[i:i+10])) for i in range(0, 40, 10)]))
```