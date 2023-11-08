```python
import Data.Time.Calendar
import Data.Time.Calendar.WeekDate

def longYear(year):
    date = Data.Time.Calendar.fromGregorian(year, 12, 28)
    week_number = Data.Time.Calendar.WeekDate.toWeekDate(date)
    w = week_number[1]
    return w > 52

def main():
    mapM_(print, filter(longYear, [year for year in range(2000, 2101)]))
```