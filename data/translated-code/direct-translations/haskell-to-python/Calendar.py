```python
import Data.Text as T
import Data.Time
import Data.Time.Calendar
import Data.Time.Calendar.WeekDate
from Data.List.Split import chunksOf
import Data.List

data Day = Su | Mo | Tu | We | Th | Fr | Sa
           deriving (Show, Eq, Ord, Enum)

data Month = January | February | March
           | April   | May      | June
           | July    | August   | September
           | October | November | December
             deriving (Show, Eq, Ord, Enum)

def monthToInt(month):
    return (month.value + 1)

def dayFromDate(year, month, day):
    day_ = toWeekDate(fromGregorian(year, monthToInt(month), day))[2]
    return day_ % 7

def nSpaces(n):
    return T.replicate(n, " ")

space = nSpaces(1)

calMarginWidth = 3

calMargin = nSpaces(calMarginWidth)

calWidth = 20

def listMonth(year, month):
    monthHeader = T.center(calWidth, " ") + T.pack(str(month))
    weekHeader = T.intercalate(space, list(map(str, list(Day))))
    monthLength = toInteger(gregorianMonthLength(year, monthToInt(month)))
    firstDay = dayFromDate(year, month, 1)
    days = [nSpaces(2)] * firstDay + list(map(lambda x: T.justifyRight(2, " ") + T.pack(str(x)), list(range(1, monthLength + 1))))
    weeks = list(map(lambda x: T.justifyLeft(calWidth, " ") + T.intercalate(space, x), chunksOf(7, days)))
    weeks_ = weeks + [nSpaces(calWidth)] * (6 - len(weeks))
    return [monthHeader, weekHeader] + weeks_

def listCalendar(year, calColumns):
    return chunksOf(calColumns, list(map(lambda x: listMonth(year, x), list(Month))))

def calColFromCol(columns):
    c, r = divmod(columns, (calWidth + calMarginWidth))
    return c + 1 if r >= calWidth else c

def colFromCalCol(calCol):
    return calCol * calWidth + ((calCol - 1) * calMarginWidth)

def center(i, a):
    return T.unpack(T.center(i, " ") + T.pack(a))

def printCal(c):
    for rows in map(lambda x: T.intercalate(calMargin, x), transpose(c)):
        print(T.unpack(rows))

def printCalendar(year, columns):
    if columns < 20:
        print("Cannot print less than 20 columns")
    else:
        print(center(columns_, "[Maybe Snoopy]"))
        print(center(columns_, str(year)))
        print("")
        printCal(listCalendar(year, calcol_))
    calcol_ = calColFromCol(columns)
    columns_ = colFromCalCol(calcol_)
```