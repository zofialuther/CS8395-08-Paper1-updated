```python
def expand_range(input_str):
    result = []
    ranges = input_str.split(',')
    for r in ranges:
        if '-' in r:
            start, end = map(int, r.split('-'))
            result.extend(range(start, end+1))
        else:
            result.append(int(r))
    return sorted(result)
```