import Data.IORef
import Data.HashMap.Strict as HashMap
import qualified Control.Monad as M

frequencies :: [Text] -> IO (HashMap Text (IORef Int))
frequencies list = do
  foldM (\acc x -> alterF alter acc x) HashMap.empty list
  where
    alter Nothing = newIORef 1
    alter (Just ref) = modifyIORef ref (+1)

main :: IO ()
main = do
  args <- getArgs
  when (length args /= 1) $ error "Exactly 1 argument is required"
  let maxw = read $ head args
  content <- T.getLine
  let words = map T.toLower $ filter (not . T.null) $ T.words content
  freqTable <- frequencies words
  topWords <- mapM (\(_, ref) -> readIORef ref) $ take maxw $ sortOn (Down . snd) $ HashMap.toList freqTable
  print topWords