```python
from itertools import count

def a131382():
    return (index for index, value in enumerate(map(lambda x: productDigitSums(x), count(1))) if index == value)

def productDigitSums(n):
    return [digitSum(n * i) for i in range(10)]

def main():
    result = [str(x) for x in list(a131382())[:40]]
    result = [result[i:i+10] for i in range(0, len(result), 10)]
    print(table(" ", result))

def digitSum(n):
    if n == 0:
        return 0
    else:
        return digitSum(n // 10) + (n % 10)

def table(gap, rows):
    max_length = [max([len(x) for x in col]) for col in zip(*rows)]
    return "\n".join([gap.join([f'{x:{length}s}' for x, length in zip(row, max_length)]) for row in rows])
```