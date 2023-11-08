from PIL import Image, ImageDraw

# Create a new image with RGB format and size of (256, 256)
img = Image.new("RGB", (256, 256))

# Initialize a drawing tool to draw on the image
draw = ImageDraw.Draw(img)

# Loop through x from 0 to 255
for x in range(256):
    # Loop through y from 0 to 255
    for y in range(256):
        # Use the drawing tool to set the color of the pixel at position (x, y) to (0, x^y, 0)
        draw.point((x, y), (0, x^y, 0))

# Delete the drawing tool
del draw

# Save the image as "xorpic.png" in PNG format
img.save("xorpic.png", "PNG")