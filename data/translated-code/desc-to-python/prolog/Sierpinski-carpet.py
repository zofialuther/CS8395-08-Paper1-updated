```python
import svgwrite

def write_sierpinski_carpet(file_name, size, order):
    with open(file_name, 'w') as file:
        dwg = svgwrite.Drawing(file_name, (size, size))
        dwg.add(dwg.rect(insert=(0, 0), size=(size, size), fill='white'))
        sierpinski_carpet(dwg, 0, 0, size, order)
        dwg.save()

def sierpinski_carpet(dwg, x, y, size, order):
    if order > 0:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    sierpinski_carpet(dwg, x + i * new_size, y + j * new_size, new_size, order - 1)
                    write_square(dwg, x + i * new_size, y + j * new_size, new_size)

def write_square(dwg, x, y, size):
    dwg.add(dwg.rect(insert=(x, y), size=(size, size), fill='black'))
```