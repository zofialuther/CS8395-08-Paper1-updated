```python
from functools import reduce

def harshads():
    return list(filter(lambda x: (x % digitSum(x)) == 0, range(1, 10000)))

def digitSum(n):
    return reduce(lambda x, y: x + y, [int(x) for x in str(n)])

def main():
    print(list(harshads()[:20]))
    print(list(filter(lambda x: x > 1000, harshads()))[:1])

main()
```