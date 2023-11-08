```python
def o(O):
    return O in [0, 1, 2, 3, 4, 5, 6, 7]

def octal(O):
    return all(oct_digit in [0, 1, 2, 3, 4, 5, 6, 7] for oct_digit in O)

def octalize():
    for O in range(0, 1000):
        if octal([int(d) for d in str(O)]):
            print(oct(O))
```