import System.Environment
import Control.Concurrent
import Control.Concurrent.Async

sleepSort :: [Int] -> IO ()
sleepSort xs = mapConcurrently_ (\x -> do
    threadDelay (x * 10^4)
    print x
    ) xs

main :: IO ()
main = do
    args <- getArgs
    let nums = map read args
    sleepSort nums