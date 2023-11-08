```python
from datetime import timedelta, datetime

def five_weekends_per_month(start_date, stop_date):
    result = []
    current_date = start_date
    while current_date <= stop_date:
        num_weekends = 0
        month = current_date.month
        while current_date.month == month:
            if current_date.weekday() in [5, 6]:
                num_weekends += 1
            current_date += timedelta(days=1)
        if num_weekends >= 15:
            result.append(datetime(current_date.year, month, 1))
    return result

start_date = datetime(2022, 1, 1)
stop_date = datetime(2022, 12, 31)
months_with_five_weekends = five_weekends_per_month(start_date, stop_date)

for i in range(5):
    print(months_with_five_weekends[i].strftime("%B %Y"))

for i in range(len(months_with_five_weekends)-5, len(months_with_five_weekends)):
    print(months_with_five_weekends[i].strftime("%B %Y"))
```