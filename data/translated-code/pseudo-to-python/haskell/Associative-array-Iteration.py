import Data.Map as M

myMap = M.fromList([("hello", 13), ("world", 31), ("!", 71)])

main :: IO ()
main = do
  let operations = M.toList <*> M.keys <*> M.elems
  operations myMap