```python
from functools import reduce

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))

def additive_persistence(n):
    count = 0
    while n >= 10:
        n = sum(map(int, str(n)))
        count += 1
    return count

def main(numbers):
    print("Number\tDigital Root\tAdditive Persistence")
    for num in numbers:
        print(f"{num}\t{digital_root(num)}\t\t{additive_persistence(num)}")

def until(condition, function, value):
    while not condition(value):
        value = function(value)
    return value
```