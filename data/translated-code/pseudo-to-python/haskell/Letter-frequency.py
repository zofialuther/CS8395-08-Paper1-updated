import Data.List
import Data.Map.Strict as M
import Data.Ord

charCounts :: String -> M.Map Char Int
charCounts = foldr (M.alter (Just . maybe 1 (+1))) M.empty

main :: IO ()
main = do
    contents <- readFile "miserables.txt"
    mapM_ print $ sortBy (comparing snd) $ M.toList $ charCounts contents