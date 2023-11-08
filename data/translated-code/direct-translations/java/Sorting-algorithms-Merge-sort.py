```python
def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    right = merge_sort(right)
    left = merge_sort(left)
    result = merge(left, right)

    return result


def merge(left, right):
    result = []
    it1 = iter(left)
    it2 = iter(right)

    x = next(it1)
    y = next(it2)

    while True:
        if x <= y:
            result.append(x)
            try:
                x = next(it1)
            except StopIteration:
                result.append(y)
                result.extend(it2)
                break
        else:
            result.append(y)
            try:
                y = next(it2)
            except StopIteration:
                result.append(x)
                result.extend(it1)
                break

    return result
```