import Data.ByteString.Char8 (ByteString, unpack)
import Data.Conduit
import Data.Conduit.Binary (sourceHandle, sinkHandle)
import Data.Conduit.List (mapMC, fold)
import Data.Conduit.Text (charUtf8, encodeUtf8)
import Data.Conduit.Combinators (yieldMany, map, fold)

shuffleBS :: Int -> ByteString -> IO ByteString
shuffleBS n s =
  yieldMany (unpack s)
  .| shuffleC n
  .| map charUtf8
  .| foldC

main :: IO ()
main =
  sourceHandle stdin
  .| mapMC (shuffleBS 10)
  .| sinkHandle stdout