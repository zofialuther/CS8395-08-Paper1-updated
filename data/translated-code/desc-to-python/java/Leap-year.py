```python
import calendar

def is_leap_year(year):
    return (calendar.isleap(year) and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))

years = [2000, 2004, 2100, 2400]

for year in years:
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
```