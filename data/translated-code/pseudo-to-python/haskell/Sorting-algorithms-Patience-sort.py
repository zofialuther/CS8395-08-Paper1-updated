```python
from typing import List
import Data.Array.ST as ST

newtype Pile = Pile { elements :: [Int] }

instance Eq Pile where
  (Pile (x:_)) == (Pile (y:_)) = x == y
  _ == _ = False

instance Ord Pile where
  compare (Pile (x:_)) (Pile (y:_)) = compare x y

patienceSort :: [Int] -> [Int]
patienceSort xs = mergePiles $ sortIntoPiles xs

sortIntoPiles :: [Int] -> [Pile]
sortIntoPiles xs = runST $ do
  piles <- newArray (0, length xs) []
  let
    bsearchPiles :: Int -> Int -> Int -> STArray s Int [Int] -> ST s Int
    bsearchPiles lo hi x arr = do
      if lo == hi
        then return lo
        else do
          let mid = (lo + hi) `div` 2
          pile <- readArray arr mid
          case compare (head pile) x of
            GT -> bsearchPiles lo mid x arr
            _  -> bsearchPiles (mid + 1) hi x arr
    f :: Int -> Int -> STArray s Int [Int] -> ST s ()
    f i x arr = do
      pos <- bsearchPiles 0 i x arr
      piles' <- readArray arr pos
      writeArray arr pos (x:piles')
  mapM_ (uncurry $ f (length xs) piles) $ zip xs [0..]
  elems <- getElems piles
  return $ map Pile elems

mergePiles :: [Pile] -> [Int]
mergePiles piles = unfoldr go piles
  where
    go :: [Pile] -> Maybe (Int, [Pile])
    go [] = Nothing
    go ps = let (Pile (x:xs), ps') = removeMin ps in Just (x, ps')

main :: IO ()
main = print $ patienceSort [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
```