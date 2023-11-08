```python
import Control.Monad

main = do
  forM_ [1..5] $ \i -> do
    forM_ [1..(5-i)] $ \_ -> putStr " "
    forM_ [1..(2*i-1)] $ \_ -> putStr "*"
    putStrLn ""
```