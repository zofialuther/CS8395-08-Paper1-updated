import Data.ByteString.Lazy.Char8 as C

main :: IO ()
main = do
  cs <- C.readFile "data.txt"
  mapM_ print =<<
    (C.lines cs >>=
      mapM_ (\x -> do
                let wordsList = C.words x
                let lastWord = C.unpack $ last wordsList
                let floatValue = read lastWord :: Float
                if floatValue > 6
                  then return x
                  else return C.empty
            )
    )