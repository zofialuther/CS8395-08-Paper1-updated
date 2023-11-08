import bitmap
import bitmapIO

def write():
    all_black = bitmap.new_bitmap([50, 50], [0, 0, 0])
    almost_all_black = bitmap.set_pixel0(all_black, [25, 25], [255, 255, 255])
    bitmapIO.write_ppm_p6('AlmostAllBlack.ppm', almost_all_black)