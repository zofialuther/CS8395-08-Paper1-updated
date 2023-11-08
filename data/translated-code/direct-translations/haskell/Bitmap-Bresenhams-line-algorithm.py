```python
import Bitmap
from Data.STRef import newSTRef, readSTRef, modifySTRef

def line(i, (xa, ya), (xb, yb), c):
    yV = newSTRef(ya)
    errorV = newSTRef(deltax // 2)
    for x in range(xa, xb+1):
        y = readSTRef(yV)
        i.setPix((y, x) if abs(yb - ya) > abs(xb - xa) else (x, y), c)
        modifySTRef(errorV, lambda x: x - deltay)
        error = readSTRef(errorV)
        if error < 0:
            modifySTRef(yV, lambda x: x + ystep)
            modifySTRef(errorV, lambda x: x + deltax)

    steep = abs(yb - ya) > abs(xb - xa)
    (xa_, ya_, xb_, yb_) = (ya, xa, yb, xb) if steep else (xa, ya, xb, yb)
    (x1, y1, x2, y2) = (xb_, yb_, xa_, ya_) if xa_ > xb_ else (xa_, ya_, xb_, yb_)
    deltax = x2 - x1
    deltay = abs(y2 - y1)
    ystep = 1 if y1 < y2 else -1
```