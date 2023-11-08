```python
def generate_zigzag_array(size):
    array = [[0 for i in range(size)] for j in range(size)]
    x, y = 0, 0
    for i in range(1, size * size + 1):
        array[y][x] = i
        if (x + y) % 2 == 0:
            if y == size - 1:
                x += 1
            elif x == 0:
                y += 1
            else:
                x -= 1
                y += 1
        else:
            if x == size - 1:
                y += 1
            elif y == 0:
                x += 1
            else:
                x += 1
                y -= 1
    return array
```