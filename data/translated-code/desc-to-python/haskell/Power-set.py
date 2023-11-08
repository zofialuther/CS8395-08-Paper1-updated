```python
import Data.Set
import Control.Monad

powerset :: Ord a => Set a -> Set (Set a)
powerset s = fromList $ listPowerset $ toList s

listPowerset :: [a] -> [[a]]
listPowerset = filterM (const [True, False])
```