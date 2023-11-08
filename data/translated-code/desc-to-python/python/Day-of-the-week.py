```python
import datetime

def find_sundays(start_year, end_year):
    sundays = []
    for year in range(start_year, end_year + 1):
        if datetime.date(year, 12, 25).weekday() == 6:
            sundays.append(year)
    return sundays

sundays_list = find_sundays(2008, 2121)
print("Years when December 25th is a Sunday:", sundays_list)
print("Total count:", len(sundays_list))
```