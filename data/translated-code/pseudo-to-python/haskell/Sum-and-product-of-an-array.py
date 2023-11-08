import Data.Array

main :: IO ()
main = mapM_ print $ [sum, product] <*> [elems $ listArray (1, 10) [11 .. 20]]