```python
import Data.List
import Control.Monad
import Control.Arrow

def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def leaptext(year):
    return if isleap(year) then "Leap Year" else "Not a Leap Year"
```