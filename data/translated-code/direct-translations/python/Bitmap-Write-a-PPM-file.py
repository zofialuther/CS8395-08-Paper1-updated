```python
import io

class Bitmap:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.map = [[color for _ in range(width)] for _ in range(height)]

    def fillrect(self, x, y, w, h, color):
        for i in range(x, x+w):
            for j in range(y, y+h):
                self.map[j][i] = color

    def set(self, x, y, color):
        self.map[y][x] = color

    def get(self, x, y):
        return self.map[y][x]

    def writeppmp3(self, f):
        self.writeppm(f, ppmformat='P3')

    def writeppm(self, f, ppmformat='P6'):
        assert ppmformat in ['P3', 'P6'], 'Format wrong'
        magic = ppmformat + '\n'
        comment = '# generated from Bitmap.writeppm\n'
        maxval = max(max(max(bit) for bit in row) for row in self.map)
        assert ppmformat == 'P3' or 0 <= maxval < 256, 'R,G,B must fit in a byte'
        if ppmformat == 'P6':
            fwrite = lambda s: f.write(bytes(s, 'UTF-8'))
            maxval = 255
        else:
            fwrite = f.write
            numsize = len(str(maxval))
        fwrite(magic)
        fwrite(comment)
        fwrite('%i %i\n%i\n' % (self.width, self.height, maxval))
        for h in range(self.height-1, -1, -1):
            for w in range(self.width):
                r, g, b = self.get(w, h)
                if ppmformat == 'P3':
                    fwrite('   %*i %*i %*i' % (numsize, r, numsize, g, numsize, b))
                else:
                    fwrite(bytes([r, g, b]))
            if ppmformat == 'P3':
                fwrite('\n')

# Draw something simple
black = (0, 0, 0)
white = (255, 255, 255)
bitmap = Bitmap(4, 4, black)
bitmap.fillrect(1, 0, 1, 2, white)
bitmap.set(3, 3, (127, 0, 63))

# String masquerading as ppm file (version P3)
ppmfileout = io.StringIO('')
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())

# Write a P6 file
with open('tmp.ppm', 'wb') as ppmfileout:
    bitmap.writeppm(ppmfileout)
```