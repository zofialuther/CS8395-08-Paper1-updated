```python
def floyd(xs):
    n = len(xs) + 1
    if n < 2:
        return [1]
    else:
        return list(range((n * (n - 1)) // 2 + 1, (n * (n + 1)) // 2 + 1))

def floyds():
    result = [1]
    while True:
        yield result
        result = floyd(result)

# Test
if __name__ == "__main__":
    for i, row in enumerate(floyds()):
        print(row)
        if i >= 13:
            break
```