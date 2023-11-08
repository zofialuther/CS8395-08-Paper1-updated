def main():
    SundayList = []
    christmas_days_falling_on_sunday(2011, 2121, SundayList)
    print(SundayList)

def christmas_days_falling_on_sunday(StartYear, EndYear, SundayList):
    YearRangeList = list(range(StartYear, EndYear + 1))
    SundayList.extend(filter_years_with_christmas_on_sunday(YearRangeList))

def is_christmas_day_a_sunday(Year):
    import datetime
    Date = datetime.date(Year, 12, 25)
    DayOfTheWeek = Date.weekday()
    return DayOfTheWeek == 6  # Python's date.weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday.