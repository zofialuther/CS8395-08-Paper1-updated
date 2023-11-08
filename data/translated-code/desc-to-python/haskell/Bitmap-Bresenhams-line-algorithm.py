```python
import Control.Monad.ST
import Data.Array.ST
import Data.Array
import Control.Monad

line :: Array (Int, Int) Color -> (Int, Int) -> (Int, Int) -> Color -> ST s ()
line img (x1, y1) (x2, y2) color = do
  let steep = abs (y2 - y1) > abs (x2 - x1)
      ((x1', y1'), (x2', y2')) 
        | steep     = ((y1, x1), (y2, x2))
        | otherwise = ((x1, y1), (x2, y2))
      ((dx, dy), (dErr1, dErr2))
        | x1' < x2' = ((x2' - x1'), abs (y2' - y1'), abs (y2' - y1') * 2, abs (x2' - x1') * 2) 
        | otherwise = ((x1' - x2'), abs (y2' - y1'), abs (y2' - y1') * 2, abs (x2' - x1') * 2)
  if steep 
    then forM_ [x1' .. x2'] $ \x -> do
           let y = y1' + (x - x1') * dy `div` dx
           writeArray img (y, x) color
    else forM_ [x1' .. x2'] $ \x -> do
           let y = y1' + (x - x1') * dy `div` dx
           writeArray img (x, y) color
```