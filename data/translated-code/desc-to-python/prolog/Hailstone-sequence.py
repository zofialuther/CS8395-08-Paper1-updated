```python
def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

X = hailstone_sequence(27)
print(len(X) == 112)
print(X[:4] == [27, 82, 41, 124])
print(X[-4:] == [8, 4, 2, 1])
```