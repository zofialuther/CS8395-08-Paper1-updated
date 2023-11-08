```python
def mid3digits(n):
    m = abs(n)
    s = str(m)
    if 100 > m:
        return 'Less than 3 digits'
    elif len(s) % 2 == 0:
        return 'Even digit count'
    else:
        return s[(len(s) - 3) // 2: (len(s) - 3) // 2 + 3]
```