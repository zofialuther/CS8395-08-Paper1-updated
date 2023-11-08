```python
import itertools

def count(x, lst):
    return lst.count(x)

def allBaseNNumsOfLength(n):
    return list(itertools.product(range(n), repeat=n))

def isSelfDescribing(lst):
    for i in range(len(lst)):
        if count(i, lst) != lst[i]:
            return False
    return True

def decimalize(lst):
    return int(''.join(map(str, lst)), len(lst))

def main():
    for i in range(1, 9):
        nums = filter(lambda x: isSelfDescribing(x), allBaseNNumsOfLength(i))
        result = ''.join(map(str, [decimalize(num) for num in nums]))
        print(result)

main()
```