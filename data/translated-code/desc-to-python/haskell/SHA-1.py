```python
import Data.Digest.Pure.SHA

module Digestor 
    ( convertString
    , convertToSHA1
    ) where

convertString :: String -> ByteString
convertString = Data.Digest.Pure.SHA.bytestringDigest . Data.Digest.Pure.SHA.sha1 . pack

convertToSHA1 :: String -> String
convertToSHA1 = show . Data.Digest.Pure.SHA.sha1 . pack

main :: IO ()
main = do
    let hash = convertToSHA1 "Rosetta Code"
    print hash
```