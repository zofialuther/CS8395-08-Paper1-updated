```python
import bitmap
import bitmapIO

# Create a new bitmap with dimensions of 50x50 and all black pixels
new_bitmap = bitmap.Bitmap(50, 50)

# Set a single pixel at coordinates (25,25) to white
new_bitmap.set_pixel(25, 25, bitmap.Color(255, 255, 255))

# Write the AlmostAllBlack bitmap to a PPM file called "AlmostAllBlack.ppm"
bitmapIO.write_ppm_p6(new_bitmap, "AlmostAllBlack.ppm")
```