```python
class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm_p3(self, file):
        file.write("P3\n{} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for r, g, b in row:
                file.write("{} {} {} ".format(r, g, b))
            file.write("\n")

    def write_ppm_p6(self, file):
        file.write("P6\n{} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for r, g, b in row:
                file.write(bytes([r, g, b]))

# Example usage
import io
bitmap = Bitmap(3, 3)
bitmap.set_pixel(0, 0, (255, 0, 0))
bitmap.set_pixel(1, 1, (0, 255, 0))
bitmap.set_pixel(2, 2, (0, 0, 255))

string_io = io.StringIO()
bitmap.write_ppm_p3(string_io)
print(string_io.getvalue())

with open("output.ppm", "wb") as f:
    bitmap.write_ppm_p6(f)
```