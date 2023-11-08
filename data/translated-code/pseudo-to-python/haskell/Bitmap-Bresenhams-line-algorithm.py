```python
import Bitmap
import Control.Monad
import Control.Monad.ST
import Data.STRef

var = Data.STRef.newSTRef
get = Data.STRef.readSTRef
mutate = Data.STRef.modifySTRef

def line(i, Pixel (xa, ya), Pixel (xb, yb), c):
    yV = var(ya)
    errorV = var((xb - xa) // 2)
    for x in range(xa, xb):
        y = get(yV)
        setPix(i, Pixel(y, x) if steep else Pixel(x, y), c)
        mutate(errorV, - (yb - ya))
        error = get(errorV)
        if error < 0:
            mutate(yV, y + 1)
            mutate(errorV, (xb - xa) + error)

```