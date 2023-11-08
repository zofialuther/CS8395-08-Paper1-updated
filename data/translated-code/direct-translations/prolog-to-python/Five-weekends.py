```python
from datetime import date, timedelta

def main():
    FiveWeekendList, RemainderWeekendList = weekends(1900, 2100)

    FiveLen = len(FiveWeekendList)
    print("Total five weekend months:", FiveLen)

    FirstFiveList = FiveWeekendList[:5]
    print("First five {year,month} pairs:", FirstFiveList)

    LastFiveList = FiveWeekendList[-5:]
    print("Last five {year,month} pairs:", LastFiveList)

    FiveYearList = [pair[0] for pair in FiveWeekendList]
    FiveYearSet = set(FiveYearList)

    RemainderYearList = [pair[0] for pair in RemainderWeekendList]
    RemainderYearSet = set(RemainderYearList)

    NonFiveWeekendSet = RemainderYearSet - FiveYearSet
    NonFiveWeekendLen = len(NonFiveWeekendSet)

    print("Total years with no five weekend months:", NonFiveWeekendLen)
    print(NonFiveWeekendSet)

def weekends(StartYear, EndYear):
    YearList = list(range(StartYear, EndYear+1))
    MonthList = list(range(1, 13))
    YearMonthList = pair(YearList, MonthList)
    FiveWeekendList, RemainderWeekendList = partition(has_five_weekends, YearMonthList)
    return FiveWeekendList, RemainderWeekendList

def has_five_weekends(pair):
    Year, Month = pair
    if long_month(Month) and starts_on_a_friday(Year, Month):
        return True
    else:
        return False

def starts_on_a_friday(year, month):
    first_day = date(year, month, 1)
    day_of_week = first_day.weekday()
    if day_of_week == 4:
        return True
    else:
        return False

def take_year(pair):
    return pair[0]

def long_month(month):
    return month in [1, 3, 5, 7, 8, 10, 12]

# Helpers

def pair(L1, L2):
    return [{A,B} for A in L1 for B in L2]

def partition(func, data):
    trues = []
    falses = []
    for item in data:
        if func(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses
```