```python
# Python equivalent of the Java program FiveFSS

import calendar

def main():
    years_with_no_five_weekend_months = []
    for year in range(1900, 2101):
        num_five_weekend_months = 0
        for month in range(1, 13):
            if calendar.monthrange(year, month)[1] == 31 and calendar.weekday(year, month, 1) == 4:
                num_five_weekend_months += 1
        if num_five_weekend_months == 0:
            years_with_no_five_weekend_months.append(year)
        else:
            print(f"Year {year} has {num_five_weekend_months} months with five weekends.")
    print(f"The total number of months with five weekends is {12 * (2100 - 1900 + 1) - sum(len(calendar.month_name) for year in years_with_no_five_weekend_months)}")
    print(f"The specific years with no five weekend months are {years_with_no_five_weekend_months}")

if __name__ == "__main__":
    main()
```