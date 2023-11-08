```python
import calendar

start_year = 1900
end_year = 2100

five_weekend_months = []
lean_years = []

for year in range(start_year, end_year+1):
    five_weekend_count = 0
    for month in range(1, 13):
        if calendar.monthrange(year, month)[0] == 4 and calendar.monthrange(year, month)[1] == 31:
            five_weekend_count += 1
            five_weekend_months.append((year, month))
    if five_weekend_count == 0:
        lean_years.append(year)

print("Total number of five-weekend months:", len(five_weekend_months))
print("First five-weekend month:", five_weekend_months[0])
print("Last five-weekend month:", five_weekend_months[-1])
print("Number of lean years:", len(lean_years))
print("List of lean years:", lean_years)
```