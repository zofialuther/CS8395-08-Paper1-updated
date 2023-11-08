import System.Environment
import System.Directory
import System.FilePath.Find

main = do
    args <- getArgs
    currentDir <- getCurrentDirectory
    let pattern = head args
    files <- find always (fileName ~~? pattern) currentDir
    mapM_ putStrLn files