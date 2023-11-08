```python
import os

class PPMWriter:
    def bitmapToPPM(self, file, bitmap):
        os.remove(file)

        with open(file, 'ab') as f:
            header = "P6\n{} {}\n255\n".format(bitmap.getWidth(), bitmap.getHeight())
            f.write(header.encode('ascii'))

            for y in range(bitmap.getHeight()):
                for x in range(bitmap.getWidth()):
                    pixel = bitmap.getPixel(x, y)
                    f.write(bytes([pixel.getRed(), pixel.getGreen(), pixel.getBlue()]))
```