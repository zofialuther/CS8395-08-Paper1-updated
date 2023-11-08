import Control.Monad

main = do
  forM_ [1024, 512..1] $ \x -> do
    if x > 0
      then print (x / 2)
      else return()