def main():
    FiveWeekendList, RemainderWeekendList = weekends(1900, 2100)

    FiveLen = len(FiveWeekendList)
    print("Total five weekend months:", FiveLen)

    FirstFiveList = FiveWeekendList[:5]
    print("First five {year,month} pairs:", FirstFiveList)

    LastFiveList = FiveWeekendList[-5:]
    print("Last five {year,month} pairs:", LastFiveList)

    FiveYearList = list(map(take_year, FiveWeekendList))
    FiveYearSet = set(FiveYearList)

    RemainderYearList = list(map(take_year, RemainderWeekendList))
    RemainderYearSet = set(RemainderYearList)

    NonFiveWeekendSet = RemainderYearSet - FiveYearSet
    NonFiveWeekendLen = len(NonFiveWeekendSet)

    print("Total years with no five weekend months:", NonFiveWeekendLen)
    print(NonFiveWeekendSet)


def weekends(StartYear, EndYear):
    YearList = list(range(StartYear, EndYear + 1))
    MonthList = list(range(1, 13))
    YearMonthList = pair(YearList, MonthList)
    return partition(has_five_weekends, YearMonthList)


def has_five_weekends(YearMonth):
    Year, Month = YearMonth
    if long_month(Month) and starts_on_a_friday(Year, Month):
        return True
    else:
        return False


def starts_on_a_friday(Year, Month):
    Date = datetime.date(Year, Month, 1)
    DayOfTheWeek = Date.weekday()
    if DayOfTheWeek == 4:
        return True
    else:
        return False


def take_year(YearMonth):
    return YearMonth[0]


def long_month(Month):
    return Month in [1, 3, 5, 7, 8, 10, 12]


def pair(L1, L2):
    return [{"Year": A, "Month": B} for A in L1 for B in L2]


def slice(List, N):
    if N == 0:
        return []
    elif N < 0:
        return List[-abs(N):]
    else:
        return List[:N]