import Data.List (sortBy)
import Data.Map.Strict as M
import Data.Ord (comparing)

charCounts :: String -> M.Map Char Int
charCounts = foldr (M.alter f) M.empty
  where
    f (Just x) = Just (succ x)
    f _ = Just 1

main :: IO ()
main = do
  contents <- readFile "miserables.txt"
  let result = sortBy (flip $ comparing snd) . M.toList . charCounts $ contents
  mapM_ print result