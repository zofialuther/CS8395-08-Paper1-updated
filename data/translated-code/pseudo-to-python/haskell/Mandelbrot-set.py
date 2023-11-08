```python
def iterate_values():
    for y in range(1, -1, -0.02):
        for x in range(-2, 0.5, 0.02):
            a = 0
            b = 0
            for i in range(500):
                a, b = a * a - b * b + x, 2 * a * b + y
                if a * a + b * b >= 4:
                    print(' ', end='')
                    break
            else:
                print('*', end='')
        print()
```