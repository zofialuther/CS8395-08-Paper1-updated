import System.Environment

main = do
    args <- getArgs
    putStrLn ("Program: " ++ (head args))