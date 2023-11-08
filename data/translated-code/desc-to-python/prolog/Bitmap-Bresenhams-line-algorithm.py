```python
import numpy as np
import matplotlib.pyplot as plt

def draw_recursive_line(image, x1, y1, x2, y2, color):
    # base case: if the two points are the same, set the pixel color and return
    if x1 == x2 and y1 == y2:
        image[y1, x1] = color
        return
    else:
        # calculate the midpoint between the two points
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        # recursively draw the two half-lines
        draw_recursive_line(image, x1, y1, mx, my, color)
        draw_recursive_line(image, mx, my, x2, y2, color)

def draw_line(image, x1, y1, x2, y2, color):
    # calculate the differences in x and y coordinates
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # call the recursive line drawing function
    draw_recursive_line(image, x1, y1, x2, y2, color)

def init(width, height, x1, y1, x2, y2):
    # create a new bitmap image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    # draw a line on the image
    draw_line(image, x1, y1, x2, y2, (255, 255, 255))
    # save the image as a .ppm file
    plt.imsave('output_image.ppm', image)
```