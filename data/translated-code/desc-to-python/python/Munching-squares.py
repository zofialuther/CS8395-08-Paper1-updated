```python
from PIL import Image, ImageDraw

# Create a new 256x256 pixel RGB image
img = Image.new('RGB', (256, 256))

# Create a draw object
draw = ImageDraw.Draw(img)

# Iterate through each pixel and apply color based on XOR operation
for x in range(256):
    for y in range(256):
        color = (x ^ y, x ^ y, x ^ y)
        draw.point((x, y), fill=color)

# Save the resulting image as "xorpic.png" in the PNG format
img.save('xorpic.png', 'PNG')
```