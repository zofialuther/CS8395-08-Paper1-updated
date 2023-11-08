import Control.Concurrent

main = do
  forkIO (putStrLn "Enjoy")
  forkIO (putStrLn "Rosetta")
  putStrLn "Code"