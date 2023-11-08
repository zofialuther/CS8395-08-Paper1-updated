import Data.Time

formats :: FormatTime t => [t -> String]
formats = (formatTime defaultTimeLocale) <$>  ["%F", "%A, %B %d, %Y"]

main :: IO ()
main = do
  t <- pure utcToLocalTime <*> getCurrentTimeZone <*> getCurrentTime
  putStrLn $ unlines (formats <*> pure t)