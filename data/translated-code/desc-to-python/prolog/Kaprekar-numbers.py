```python
def kaprekar(N, Result):
    for num in range(1, N+1):
        squared = num * num
        if split_number(num, squared):
            Result.append(num)

def split_number(num, squared):
    squared_str = str(squared)
    for i in range(len(squared_str)):
        part1 = int(squared_str[:i])
        part2 = int(squared_str[i:])
        if part1 + part2 == num:
            return True
    return False
```