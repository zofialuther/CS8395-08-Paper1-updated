from datetime import datetime

def isLeapYear(year):
    return (year % 100 == 0) and (year % 400 == 0) or (year % 4 == 0)

years = [1800, 1900, 1994, 1998, 1999, 2000, 2001, 2004, 2100]
for year in years:
    print(f"The year {year} is leaper: {datetime(year, 1, 1).is_leap_year()} / {isLeapYear(year)}.")