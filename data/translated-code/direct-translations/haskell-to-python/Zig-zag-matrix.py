import Data.Array
import Text.Printf

show2d a =
  unlines
    [ unwords
       [ printf("%3d" % a[x, y])
       for x in range(l, h+1) ]
    for y in range(l, h+1) ]
  where
    (l, h) = a.bounds

main = mapM_(putStr . ('\n'.join) . show2d . zigZag) [(3, 3), (4, 4), (10, 2)]