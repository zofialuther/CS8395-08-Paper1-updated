import System.Environment
import System.Directory

isEmpty :: FilePath -> IO String
isEmpty path = do
  contents <- getDirectoryContents path
  if length contents == 2
    then if "." `elem` contents && ".." `elem` contents
      then return "Directory is empty"
      else return "Directory is not empty"
    else return "Directory is not empty"

main :: IO ()
main = do
  args <- getArgs
  result <- isEmpty (head args)
  putStrLn result