```python
import math

def write_sierpinski_pentagon(file_name, size, order):
    with open(file_name, 'w') as file:
        file.write('<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(size, size))
        file.write('<rect width="100%" height="100%" fill="white"/>\n')
        dimensions = calculate_pentagon_dimensions(size)
        sierpinski_pentagon(file, dimensions, order, 0, 0, size)
        file.write('</svg>')

def calculate_pentagon_dimensions(size):
    radius = size / (2 * (1 + math.sin(math.pi / 5)))
    center_x = size / 2
    center_y = size / 2
    return (radius, center_x, center_y)

def sierpinski_pentagon(file, dimensions, order, center_x, center_y, size):
    if order == 0:
        write_pentagon_points(file, dimensions, center_x, center_y)
    else:
        radius, _, _ = dimensions
        sierpinski_pentagon(file, dimensions, order - 1, center_x, center_y, size / 3)
        for i in range(5):
            angle = 2 * math.pi * i / 5
            new_center_x = center_x + size * math.cos(angle)
            new_center_y = center_y + size * math.sin(angle)
            sierpinski_pentagon(file, dimensions, order - 1, new_center_x, new_center_y, size / 3)

def write_pentagon_points(file, dimensions, center_x, center_y):
    radius, _, _ = dimensions
    file.write('<polygon points="')
    for i in range(5):
        angle = 2 * math.pi * i / 5
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        file.write('{},{} '.format(x, y))
    file.write('" fill="black"/>\n')

write_sierpinski_pentagon('sierpinski_pentagon.svg', 500, 3)
```