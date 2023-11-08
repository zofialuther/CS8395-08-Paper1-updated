```python
{-# LANGUAGE OverloadedStrings #-}

import Data.Text
import Data.Text.IO

main = do
  let text = "Hello,How,Are,You,Today"
  let splitText = splitOn "," text
  let result = intercalate "." splitText
  putStrLn result
```