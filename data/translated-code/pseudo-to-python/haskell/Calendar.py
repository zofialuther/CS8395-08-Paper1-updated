```python
import calendar
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

def monthToInt(month):
    return month.value

def dayFromDate(year, month, day):
    return calendar.weekday(year, month, day)

def nSpaces(num):
    return " " * num

space = " "

calMarginWidth = 3
calMargin = nSpaces(calMarginWidth)
calWidth = 20

def listMonth(year, month):
    return calendar.month_name[month]

def listCalendar(year, calColumns):
    return calendar.monthcalendar(year, calColumns)

def calColFromCol(columns):
    return columns - 1

def colFromCalCol(calCol):
    return calCol + 1

def center(width, text):
    return text.center(width)

def printCal(calendar):
    for week in calendar:
        for day in week:
            print(day, end=" ")
        print()

def printCalendar(year, columns):
    cal = listCalendar(year, columns)
    printCal(cal)
```