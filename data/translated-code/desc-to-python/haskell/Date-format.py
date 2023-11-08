```python
import Data.Time
import Data.Time.Format
import Control.Monad
import System.Locale

formats = [formatTime defaultTimeLocale "%Y-%m-%d %H:%M:%S", 
           formatTime defaultTimeLocale "%H:%M:%S"]

main = do
    tz <- getCurrentTimeZone
    now <- getCurrentTime
    let localTime = utcToLocalTime tz now
    forM_ formats (\f -> putStrLn $ f localTime)
```