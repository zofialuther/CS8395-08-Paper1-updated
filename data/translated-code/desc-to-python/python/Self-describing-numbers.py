```python
def isSelfDescribing(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str.count(str(i)) != int(num_str[i]):
            return False
    return True

self_describing_nums = [num for num in range(4000001) if isSelfDescribing(num)]
result = self_describing_nums

self_describing_tuples = [(num, isSelfDescribing(num)) for num in self_describing_nums]
```