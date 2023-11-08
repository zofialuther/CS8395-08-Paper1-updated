```python
import Control.Monad
import Control.Concurrent
import Control.Concurrent.STM
import System.Random

type Fork = TMVar Int

newFork :: Int -> IO Fork
newFork i = newTMVarIO i

takeFork :: Fork -> STM Int
takeFork fork = takeTMVar fork

releaseFork :: Int -> Fork -> STM ()
releaseFork i fork = putTMVar fork i

type Name = String

runPhilosopher :: Name -> (Fork, Fork) -> IO ()
runPhilosopher name (left, right) = forever $ do
  putStrLn (name ++ " is hungry.")
  (leftNum, rightNum) <- atomically $ do
    leftNum <- takeFork left
    rightNum <- takeFork right
    return (leftNum, rightNum)
  putStrLn (name ++ " got forks " ++ show leftNum ++ " and " ++ show rightNum ++ " and is now eating.")
  delay <- randomRIO (1,10)
  threadDelay (delay * 1000000)
  putStrLn (name ++ " is done eating. Going back to thinking.")
  atomically $ do
    releaseFork leftNum left
    releaseFork rightNum right
  delay <- randomRIO (1, 10)
  threadDelay (delay * 1000000)

philosophers :: [String]
philosophers = ["Aristotle", "Kant", "Spinoza", "Marx", "Russel"]

main = do
  forks <- mapM newFork [1..5]
  let namedPhilosophers  = map runPhilosopher philosophers
      forkPairs          = zip forks (tail . cycle $ forks)
      philosophersWithForks = zipWith ($) namedPhilosophers forkPairs
  putStrLn "Running the philosophers. Press enter to quit."
  mapM_ forkIO philosophersWithForks
  getLine
```