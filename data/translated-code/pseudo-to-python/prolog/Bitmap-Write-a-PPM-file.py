```python
import bitmap
import bitmapIO

def write():
    AllBlack = bitmap.Bitmap(50, 50, [0,0,0])
    AllBlack.set_pixel(25, 25, [255,255,255])
    bitmapIO.write_ppm_p6(AllBlack, "output.ppm")
```