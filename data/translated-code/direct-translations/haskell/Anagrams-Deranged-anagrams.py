from typing import List, Tuple
import Data.List
import Data.Ord
import qualified Data.Map as M
import qualified Data.Set as S

groupBySig :: [String] -> [(String, S.Set String)]
groupBySig = map ((,) . sort <*> S.singleton)

equivs :: [(String, S.Set String)] -> [[String]]
equivs = map (S.toList . snd) . M.toList . M.fromListWith S.union

isDerangement :: (String, String) -> Bool
isDerangement (a, b) = and $ zipWith (/=) a b

pairs :: [t] -> [(t, t)]
pairs = concat . unfoldr step
  where
    step (x:xs) = Just (map (x, ) xs, xs)
    step [] = Nothing

anagrams :: [String] -> [(String, String)]
anagrams = concatMap pairs . equivs . groupBySig

maxDerangedAnagram :: [String] -> Maybe (String, String)
maxDerangedAnagram = maxByLen . filter isDerangement . anagrams
  where
    maxByLen [] = Nothing
    maxByLen xs = Just $ maximumBy (comparing (length . fst)) xs

main :: IO ()
main = do
  input <- readFile "unixdict.txt"
  case maxDerangedAnagram $ words input of
    Nothing -> putStrLn "No deranged anagrams were found."
    Just (a, b) -> putStrLn $ "Longest deranged anagrams: " <> a <> " and " <> b