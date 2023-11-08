```python
from itertools import product

def count(x, lst):
    return len([i for i in lst if i == x])

def allBaseNNumsOfLength(n):
    return list(product(range(n), repeat=n))

def isSelfDescribing(num):
    return all(x == count(i, num) for i, x in enumerate(num))

def decimalize(lst):
    return int(''.join(map(str, lst)))

def main():
    result = [decimalize(num) for num in allBaseNNumsOfLength(8) if isSelfDescribing(num)]
    print(result)

if __name__ == "__main__":
    main()
```