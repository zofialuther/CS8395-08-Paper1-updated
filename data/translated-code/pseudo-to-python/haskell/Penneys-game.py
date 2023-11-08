import Data.List as L
import System.IO
import System.Random

data CoinToss = H | T deriving (Read, Show, Eq)

parseToss :: String -> [CoinToss]
parseToss [] = []
parseToss (x:xs)
  | x == 'h' || x == 'H' = H : parseToss xs
  | x == 't' || x == 'T' = T : parseToss xs
  | otherwise = parseToss xs

notToss :: CoinToss -> CoinToss
notToss H = T
notToss T = H

instance Random CoinToss where
  random g = 
    let (b, gb) = random g
    in if b then (H, gb) else (T, gb)
  randomR = undefined

prompt :: String -> (String -> Maybe a) -> IO a
prompt message parse = do
  putStrLn message
  line <- getLine
  case parse line of
    Nothing -> do
      putStrLn "Invalid input"
      prompt message parse
    Just a -> return a

showCat :: Show a => [a] -> String
showCat = concatMap show

data Winner = Player | CPU

runToss :: [CoinToss] -> [CoinToss] -> StdGen -> ([CoinToss], Winner)
runToss playerSeq cpuSeq g = 
  let stream = randoms g
      run xs
        | isPrefixOf playerSeq xs = (playerSeq, Player)
        | isPrefixOf cpuSeq xs = (cpuSeq, CPU)
        | otherwise = (xs, CPU)
  in run stream

game :: Bool -> [CoinToss] -> [CoinToss] -> StdGen -> IO ()
game _ playerSeq cpuSeq g = do
  putStrLn "Current score"
  let (genA, genB) = split g
      promptPlayer tosses = do
        input <- prompt "Pick 3 coin sides" (Just . parseToss)
        if length input == 3
          then return input
          else promptPlayer tosses
      promptCpu _ = putStrLn "CPU's choice"
  if 
    then do
      cpuChoice <- randomR (H, T) genB
      playerChoice <- promptPlayer
      let (tossResult, winner) = runToss playerChoice [notToss cpuChoice] genA
      putStrLn "Sequence tossed: " ++ showCat tossResult
      -- handle winner and update scores
      if -- game is not over
        then game False playerSeq cpuSeq updatedGen
        else return ()
    else do
      playerChoice <- promptPlayer
      let cpuChoice = -- calculate based on player's choice
      promptCpu cpuChoice
      let (tossResult, winner) = runToss playerChoice [notToss cpuChoice] genA
      putStrLn "Sequence tossed: " ++ showCat tossResult
      -- handle winner and update scores
      if -- game is not over
        then game True playerSeq cpuSeq updatedGen
        else return ()

main :: IO ()
main = do
  hSetBuffering stdin LineBuffering
  g <- getStdGen
  cpuFirstTurn <- randomR (H, T) g
  game True [] [] g